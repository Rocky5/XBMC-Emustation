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

#include "dialogs/GUIDialogFavourites.h"
#include "dialogs/GUIDialogContextMenu.h"
#include "Favourites.h"
#include "GUIWindowManager.h"
#include "GUIDialogKeyboard.h"
#include "FileItem.h"
#include "LocalizeStrings.h"
#include "interfaces/Builtins.h"
#include "FileSystem/File.h"

using namespace XFILE;

#define FAVOURITES_LIST 450

CGUIDialogFavourites::CGUIDialogFavourites(void)
    : CGUIDialog(WINDOW_DIALOG_FAVOURITES, "DialogFavourites.xml")
{
  m_favourites = new CFileItemList;
}

CGUIDialogFavourites::~CGUIDialogFavourites(void)
{
  delete m_favourites;
}

bool CGUIDialogFavourites::OnMessage(CGUIMessage &message)
{
  if (message.GetMessage() == GUI_MSG_CLICKED)
  {
    if (message.GetSenderId() == FAVOURITES_LIST)
    {
      int item = GetSelectedItem();
      int action = message.GetParam1();
      if (action == ACTION_SELECT_ITEM || action == ACTION_MOUSE_LEFT_CLICK)
        OnClick(item);
      else if (action == ACTION_SELECT_ITEM || action == ACTION_MOUSE_LEFT_CLICK)
        OnClick(item);
      else if (action == ACTION_SELECT_ITEM || action == ACTION_MOUSE_LEFT_CLICK)
        OnClick(item);
      else if (action == ACTION_MOVE_ITEM_UP)
        OnMoveItem(item, -1);
      else if (action == ACTION_MOVE_ITEM_DOWN)
        OnMoveItem(item, 1);
      else if (action == ACTION_CONTEXT_MENU || action == ACTION_MOUSE_RIGHT_CLICK)
        OnPopupMenu(item);
      else if (action == ACTION_DELETE_ITEM)
        OnDelete(item);
      else
        return false;
      return true;
    }
  }
  else if (message.GetMessage() == GUI_MSG_WINDOW_DEINIT)
  {
    CGUIDialog::OnMessage(message);
    // clear our favourites
    CGUIMessage message(GUI_MSG_LABEL_RESET, GetID(), FAVOURITES_LIST);
    OnMessage(message);
    m_favourites->Clear();
    return true;
  }
  return CGUIDialog::OnMessage(message);
}

void CGUIDialogFavourites::OnInitWindow()
{
  CFavourites::Load(*m_favourites);
  UpdateList();
  CGUIWindow::OnInitWindow();
}

int CGUIDialogFavourites::GetSelectedItem()
{
  CGUIMessage message(GUI_MSG_ITEM_SELECTED, GetID(), FAVOURITES_LIST);
  OnMessage(message);
  return message.GetParam1();
}

void CGUIDialogFavourites::OnClick(int item)
{
  if (item < 0 || item >= m_favourites->Size())
    return;

  // grab our message, close the dialog, and send
  CFileItemPtr pItem = (*m_favourites)[item];
  CStdString execute(pItem->GetPath());

  //Close();

  CGUIMessage message(GUI_MSG_EXECUTE, 0, GetID());
  message.SetStringParam(execute);
  g_windowManager.SendMessage(message);
}

void CGUIDialogFavourites::OnPopupMenu(int item)
{
  if (item < 0 || item >= m_favourites->Size())
    return;

  // highlight the item
  (*m_favourites)[item]->Select(true);

  CContextButtons choices;
  if (CFile::Exists("special://xbmc/emustation/scripts/sort_favourites.py"))
  {
    choices.Add(1, "Sort by Name");
    choices.Add(2, "Sort by System");
  }
  if (m_favourites->Size() > 1)
  {
    choices.Add(3, 13332);
    choices.Add(4, 13333);
  }
  choices.Add(5, 15015);
  choices.Add(6, 118);
  
  int button = CGUIDialogContextMenu::ShowAndGetChoice(choices);

  // unhighlight the item
  (*m_favourites)[item]->Select(false);

  if (button == 1)
	  SortA();
  else if (button == 2)
	  SortSA();
  else if (button == 3)
    OnMoveItem(item, -1);
  else if (button == 4)
    OnMoveItem(item, 1);
  else if (button == 5)
    OnDelete(item);
  else if (button == 6)
    OnRename(item);
}

void CGUIDialogFavourites::SortSA()
{
  CBuiltins::Execute("RunScript(special://xbmc/emustation/scripts/sort_favourites.py,1)");
}

void CGUIDialogFavourites::SortA()
{
  CBuiltins::Execute("RunScript(special://xbmc/emustation/scripts/sort_favourites.py)");
}

void CGUIDialogFavourites::OnMoveItem(int item, int amount)
{
  if (item < 0 || item >= m_favourites->Size() || m_favourites->Size() <= 1 || 0 == amount) return;

  int nextItem = (item + amount) % m_favourites->Size();
  if (nextItem < 0) nextItem += m_favourites->Size();

  m_favourites->Swap(item, nextItem);
  CFavourites::Save(*m_favourites);

  CGUIMessage message(GUI_MSG_ITEM_SELECT, GetID(), FAVOURITES_LIST, nextItem);
  OnMessage(message);

  UpdateList();
}

void CGUIDialogFavourites::OnDelete(int item)
{
  if (item < 0 || item >= m_favourites->Size())
    return;
  m_favourites->Remove(item);
  CFavourites::Save(*m_favourites);

  CGUIMessage message(GUI_MSG_ITEM_SELECT, GetID(), FAVOURITES_LIST, item < m_favourites->Size() ? item : item - 1);
  OnMessage(message);
  CBuiltins::Execute("RunScript(special://xbmc/emustation/scripts/update_favs_counter.py,1)");
  UpdateList();
}

void CGUIDialogFavourites::OnRename(int item)
{
  if (item < 0 || item >= m_favourites->Size())
    return;

  CStdString label((*m_favourites)[item]->GetLabel());
  if (CGUIDialogKeyboard::ShowAndGetInput(label, g_localizeStrings.Get(16008), false))
  {
	  (*m_favourites)[item]->SetLabel(label);
	  CFavourites::Save(*m_favourites);
	  UpdateList();
  }
}

void CGUIDialogFavourites::UpdateList()
{
  int currentItem = GetSelectedItem();
  CGUIMessage message(GUI_MSG_LABEL_BIND, GetID(), FAVOURITES_LIST, currentItem >= 0 ? currentItem : 0, 0, m_favourites);
  OnMessage(message);
}

CFileItemPtr CGUIDialogFavourites::GetCurrentListItem(int offset)
{
  int currentItem = GetSelectedItem();
  if (currentItem < 0 || !m_favourites->Size()) return CFileItemPtr();

  int item = (currentItem + offset) % m_favourites->Size();
  if (item < 0) item += m_favourites->Size();
  return (*m_favourites)[item];
}

