/*
 *      Copyright (C) 2005-2013 Team XBMC
 *      http://xbmc.org
 *
 *  This Program is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation; either version 2, or (at your option)
 *  any later version.
 *
 *  This Program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with XBMC; see the file COPYING.  If not, see
 *  <http://www.gnu.org/licenses/>.
 *
 */

#include "utils/log.h"
#include "FileSystem/File.h"
#include "Favourites.h"
#include "Util.h"
#include "utils/URIUtils.h"
#include "Key.h"
#include "settings/Settings.h"
#include "FileItem.h"
#include "video/VideoInfoTag.h"
#include "settings/AdvancedSettings.h"

bool CFavourites::Load(CFileItemList &items)
{
  items.Clear();
  CStdString favourites;

  favourites = "special://xbmc/system/favourites.xml";
  if(XFILE::CFile::Exists(favourites))
    CFavourites::LoadFavourites(favourites, items);
  else
    CLog::Log(LOGDEBUG, "CFavourites::Load - no system favourites found, skipping");
  URIUtils::AddFileToFolder(g_settings.GetProfileUserDataFolder(), "favourites.xml", favourites);
  if(XFILE::CFile::Exists(favourites))
    CFavourites::LoadFavourites(favourites, items);
  else
    CLog::Log(LOGDEBUG, "CFavourites::Load - no userdata favourites found, skipping");

  return true;
}

bool CFavourites::LoadFavourites(CStdString& strPath, CFileItemList& items)
{
  TiXmlDocument doc;
  if (!doc.LoadFile(strPath))
  {
    CLog::Log(LOGERROR, "Unable to load %s (row %i column %i)", strPath.c_str(), doc.Row(), doc.Column());
    return false;
  }
  TiXmlElement *root = doc.RootElement();
  if (!root || strcmp(root->Value(), "favourites"))
  {
    CLog::Log(LOGERROR, "Favourites.xml doesn't contain the <favourites> root element");
    return false;
  }

  TiXmlElement *favourite = root->FirstChildElement("favourite");
  while (favourite)
  {
    // format:
    // <favourite name="Cool Video" thumb="foo.jpg">PlayMedia(c:\videos\cool_video.avi)</favourite>
    // <favourite name="My Album" thumb="bar.tbn">ActivateWindow(MyMusic,c:\music\my album)</favourite>
    // <favourite name="Apple Movie Trailers" thumb="path_to_thumb.png">RunScript(special://xbmc/scripts/apple movie trailers/default.py)</favourite>
    const char *name = favourite->Attribute("name");
    const char *thumb = favourite->Attribute("thumb");
    if (name && favourite->FirstChild())
    {
      if(!items.Contains(favourite->FirstChild()->Value()))
      {
        CFileItemPtr item(new CFileItem(name));
        item->SetPath(favourite->FirstChild()->Value());
        if (thumb) item->SetThumbnailImage(thumb);
        items.Add(item);
      }
    }
    favourite = favourite->NextSiblingElement("favourite");
  }
  return true;
}

bool CFavourites::Save(const CFileItemList &items)
{
  CStdString favourites;
  TiXmlDocument doc;
  TiXmlElement xmlRootElement("favourites");
  TiXmlNode *rootNode = doc.InsertEndChild(xmlRootElement);
  if (!rootNode) return false;

  for (int i = 0; i < items.Size(); i++)
  {
    const CFileItemPtr item = items[i];
    TiXmlElement favNode("favourite");
    favNode.SetAttribute("name", item->GetLabel().c_str());
    if (item->HasThumbnail())
      favNode.SetAttribute("thumb", item->GetThumbnailImage().c_str());
    TiXmlText execute(item->GetPath());
    favNode.InsertEndChild(execute);
    rootNode->InsertEndChild(favNode);
  }

  URIUtils::AddFileToFolder(g_settings.GetProfileUserDataFolder(), "favourites.xml", favourites);
  return doc.SaveFile(favourites);
}

bool CFavourites::AddOrRemove(CFileItem *item, int contextWindow)
{
  if (!item) return false;

  // load our list
  CFileItemList items;
  Load(items);

  CStdString executePath(GetExecutePath(item, contextWindow));

  CFileItemPtr match = items.Get(executePath);
  if (match)
  { // remove the item
    items.Remove(match.get());
  }
  else
  { // create our new favourite item
    CFileItemPtr favourite(new CFileItem(item->GetLabel()+" [xbox]"));
    if (item->GetLabel().IsEmpty())
      favourite->SetLabel(CUtil::GetTitleFromPath(item->GetPath(), item->m_bIsFolder));
    favourite->SetThumbnailImage(item->GetThumbnailImage());
    favourite->SetPath(executePath);
    items.Add(favourite);
  }

  // and save our list again
  return Save(items);
}

bool CFavourites::IsFavourite(CFileItem *item, int contextWindow)
{
  CFileItemList items;
  if (!Load(items)) return false;

  return items.Contains(GetExecutePath(item, contextWindow));
}

static CStdString Paramify(const CStdString& param)
{
  CStdString result(param);
  result.Replace("\\", "\\\\");
  result.Replace("\"", "\\\"");
  return "\"" + result + "\"";
}

CStdString CFavourites::GetExecutePath(const CFileItem *item, int contextWindow)
{
  CStdString execute;
  if (item->m_bIsFolder && (g_advancedSettings.m_playlistAsFolders ||
                            !(item->IsSmartPlayList() || item->IsPlayList())))
    execute.Format("ActivateWindow(%i,%s)", contextWindow, Paramify(item->GetPath()));
  else if (item->GetPath().Left(9).Equals("plugin://"))
    execute.Format("RunPlugin(%s)", Paramify(item->GetPath()));
  else if (contextWindow == WINDOW_SCRIPTS)
    execute.Format("RunScript(%s)", item->GetPath());
  else if (contextWindow == WINDOW_PROGRAMS)
    execute.Format("RunXBE(%s)", Paramify(item->GetPath()));
  else  // assume a media file
  {
    if (item->IsVideoDb() && item->HasVideoInfoTag())
      execute.Format("PlayMedia(%s)", Paramify(item->GetVideoInfoTag()->m_strFileNameAndPath));
    else
      execute.Format("PlayMedia(%s)", Paramify(item->GetPath()));
  }
  return execute;
}
