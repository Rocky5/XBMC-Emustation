Genesis Plus GX Sega Genesis/Megadrive/32X/SegaCD/MegaCD/SMS/GG Emulator for XBox v1.07b Madmab Ed

* Fixed issue where country region USA and Europe were switched.  Thus causing games to run at 50hz when Europe is selected and 60hz when USA is selected.

* Added in pixel perfect settings for SMS/GG so they should display correctly when using pixel perfect or fit to screen.  However if you use custom screen size with global set to yes there will be a mismatch between sms/gg and Genesis screens.

* A bunch of internal changes related to the sms/gg support.

---------------------------------------------------------------------------------------

Genesis Plus GX Sega Genesis/Megadrive/32X/SegaCD/MegaCD/SMS/GG Emulator for XBox v1.06b Madmab Ed

* updated to the latest Genesis Plus GX core, see below list. (thanks Xtecuter73)

* Added soft reset option to the "in-game" menu for the GX core.  A soft reset should not wipe the SRAM now.

* Fixed audio glitches when changing CDDA tracks on a Darkwater (bin/cue) image format.  This may be an issue with a bug in the buffering code which may need looking over rather than using the current fix.

* ROM images that access CDDA data (aka Sonic1 hack and Rock -n- Roll Racing hack) now work correctly.  Just do the same thing as with Pier Solar.  Make sure the cue and/or bin file has the same filename as the ROM file.  This works better with the cue file just make sure the filenames in the cue file are correct.

*******************************************
Genesis Plus GX 1.7.5 (xx/xx/xxxx) (Eke-Eke)
*******************************************

[Core/General]
---------------
* added optional dynamic allocation of cartridge/CD hardware buffer (for platforms with BSS size limitation)
* improved frame emulation timing, now starts with vertical blanking to reduce input lag by one more frame
(!!!warning: this breaks compatibility with previous savestates!!!)
* various code cleanup

[Core/CD]
---------------
* added CD-AUDIO & CD+G support
* added optional support for external VORBIS library
* added CDC & GFX register polling detection / synchronization
* improved CDC emulation (fixes random freezes during Jeopardy & ESPN Sunday Night NFL intro)
* improved emulation of mirrored memory areas
* improved savestate format
* improved Sub-CPU synchronization with Main-CPU (fixes "Soul Star")
* improved Main-CPU & Sub-CPU idle loop detection (fixes "Super League CD")
* disabled 68k and Z80 access to PRG-RAM when SUB-CPU is running (fixes USA version of Dungeon Explorer )
* disabled CD hardware reset on Soft-Reset (verified on real hardware)
* fixed DATA track minimal length (fixes BIOS refusing to boot small homebrew demos)
* fixed CDD "no disc" status code (fixes boot sequence loading time when no disc is loaded)
* fixed OGG file seeking when using with CUE file
* fixed PRG-RAM access from MAIN-CPU side on system reset
* fixed state loading bug when SUB-CPU interrupt is pending 
* fixed incorrect masking of Level 3 (GFX) interrupts (spurious freeze during Japanese BIOS intro)
* fixed H-INT vector handling when using Mode 1
* fixed access to "write-only" communication flags (verified on real hardware by Notaz)
* fixed pending level 1 interrupts when GFX interrupt is disabled (fixes random freezes out of "Batman Returns" option menu)
* fixed CDD seek command again (Final Fight CD freeze with model 2 BIOS)
* optimized Sub-CPU / Main-CPU synchronization

[Core/MD]
---------------
* added support for some new unlicensed games with copy protection (Thunderbolt II, Tom Clown, Chaoji Puke / Super Poker)
* added support for Everdrive extended SSF mapper
* improved console region auto-detection for a few PAL-only games (The Smurfs Travel the World & Williams Arcade's Greatest Hits)
* fixed Game Genie / Pro Action Replay lock-on support when Mega CD hardware is enabled 
* fixed SRAM support in Triple Play 96 & Triple Play - Gold Edition
* fixed automatic CD loading with .md ROM files
* fixed ROM padding for Sonic & Knuckles
* fixed SRAM detection for games where it is mapped to work RAM ("Feng Kuang Tao Hua Yuan" crash)
* fixed 1.7.4 regression with games using SRAM bank-switching

[Core/MS]
---------------
* added support for new SMS Power dump Jang Pung II (KR)
* added support for Hi-Com X-in-1 mapper (thanks to Bock from SMS Power)
* improved console hardware auto-detection
* improved emulation accuracy of SG-1000 & Mark-III hardware
* improved emulation accuracy of Japanese Master System I/O chip (315-5297)
* fixed Boot ROM loading when switching system hardware

[Core/GG]
---------------
* added optional LCD ghosting software filter
* fixed mirrored access to I/O control register (G-LOC Air Battle)

[Core/SG]
---------------
* added support for SG-1000 II clone hardware (2KB RAM + integrated VDP/PSG chip 315-5066)
* fixed SG-1000 internal RAM size (1KB instead of 2KB)
* restored SG-1000 Pause button support

[Core/CPU]
---------------
* fixed Z80 SP register initialization on power-on for Master System & Game Gear 
(Ace of Aces, Shadow Dancer, Ecco the Dolphin, Evander Holyfield Real Deal Boxing)

[Core/IO]
---------------
* added Sega Graphic Board support (thanks to SMS Power)
* added Master Tap emulation (multi-player support in Boom homebrew)
* added gamepad type auto-detection
* added support for XE-1AP analog controller on both ports 
* improved HVC latch behavior for gun emulation (fixes "Gunfight - 3 in 1" randomization when using Justifier)
* fixed TeamPlayer emulation (fixes multitap detection in Gauntlet 4)

[Core/VDP]
---------------
* implemented proper FIFO ring-buffer & unused bits behavior on CRAM/VSRAM reads (verified on real hardware by Nemesis)
* improved accuracy of DMA Copy/Fill & added support for CRAM/VSRAM Fill (verified on real hardware by Nemesis)
* improved V28/V30 mode switching during active display (verified on real hardware)
* improved Mode 5 sprites parsing accuracy (verified on real hardware)
* improved Mode 5 sprites rendering timings (fixes "Overdrive" demo)
* improved FIFO timings accuracy (fixes "Overdrive" Demo)
* improved H-Counter accuracy in H32 mode
* improved accuracy of Master System color palette brightness range (verified against real hardware)
* fixed misaligned buffer writes in Mode 4 when -DALIGN_LONG option is used
* fixed alpha channel for 15-bit (RGB555) and 32-bit (RGB888) color support
* fixed register #10 state on VDP¨reset (fixes GG Terminator 2: Judgment Day)
* fixed Mode 1 rendering (TMS99xx "text" mode)
* fixed Game Gear display rendering regression when left/right borders were disabled
* fixed 68k cycles delay on invalid VRAM writes (fixes "Microcosm" intro loop)
* optimized tile caching

*******************************************
Genesis Plus GX 1.7.4 (21/06/2013) (Eke-Eke)
*******************************************

[Core/SCD]
---------------
* fixed access to read-only registers on Main-CPU side ("Batman Returns" platform level freeze)
* fixed & improved emulation of PRG-RAM write protection register ("Lunar Eternal Blue" japanese version freeze)
* improved SUB & MAIN-CPU synchronization ("Dracula Unleashed" freeze when using US Model 2 BIOS)
* improved CPU polling detection
* improved CDD emulation & added CD drive access time for SEEK command ("Panic!/Switch" intro missing scene)
* added missing reinitialization of MAIN-CPU PRG-RAM bank on reset
* added .OGG audio tracks support through LIBTREMOR

[Core/Sound]
---------------
* fixed YM2612 configurable DAC depth emulation
* improved Low-Pass filter
* added optional "MONO" output mode

[Core/VDP]
---------------
* fixed FIFO access timings when using invalid write code value ("Clue" menu)
* fixed DMA Copy with undocumented code value ("Fatal Labyrinth" end sequence)
* minor code fixes & optimizations

[Core/CPU]
---------------
* optimized 68k stack read/write functions
* fixed broken 68k address error emulation
* fixed 68k interrupt behavior (prevents interrupts from being executed multiple time when 68k is halted)
* fixed Z80 registers initial state, added proper initialization when using PBC (verified on real hardware by Charles McDonald)

[Core/MD]
---------------
* fixed SRAM incompatibilities between BIG ENDIAN & LITTLE ENDIAN platforms (note: this breaks old .srm files with LITTLE ENDIAN platform ports)
* added support for a few recently dumped unlicensed games
* added auto-detection of byte-swapped ROM files

*******************************************
Genesis Plus GX 1.7.3 (26/11/2012) (Eke-Eke)
*******************************************

Nothing for the xbox.

*******************************************
Genesis Plus GX 1.7.2 (24/11/2012) (Eke-Eke)
*******************************************

[Core/SCD]
---------------
* added default TOC for Shadow of the Beast II (prevent hangs when audio tracks are missing)
* fixed CD-DA fader muting
* fixed PCM channels panning on reset
* fixed backup RAM file management when using disc swap with Mode 1 cartridge
* incremented CD drive read latency: fixes Space Adventure Cobra (freeze when opening coffin at 2nd morgue scene)
* improved CDD emulation accuracy: fixes Snatcher (freeze at the end of Act 2) & various CD player bugs
* improved MAIN-SUB memory map mirroring in SCD mode (verified on real hardware by Charles McDonald)
* implemented cycle-accurate "stopwatch" register emulation

[Core/Sound]
---------------
* fixed broken PSG noise frequency
* fixed incorrect Game Gear PSG stereo emulation
* implemented cycle-accurate Game Gear PSG stereo

[Core/VDP]
---------------
* fixed broken VDP DMA from SVP ROM latency (graphic errors in Virtua Racing)

[Core/MD]
---------------
* added Super Mario World 64 (unlicensed) cartridge hardware emulation

[Core/Input]
---------------
* added automatic detection for CD games with Justifier/Menacer support
* improved Justifier/Menacer emulation

-----------------------------------------------------------------------------------------------------

Genesis Plus GX Sega Genesis/Megadrive/32X/SegaCD/MegaCD/SMS/GG Emulator for XBox v1.05b Madmab Ed

* Fixed issue where sram was not being saved when running cartridges that access a CD (aka Pier Solar).  BTW if you want to hear the music tracks for Pier Solar.  Rename the FIRST track to match the name of your ROM image.  So if your rom is named "Pier Solar.bin" then rename the FIRST track of the cd image to "Pier Solar.iso".  This currently only works if both images are on your xbox hard drive.

-----------------------------------------------------------------------------------------------------

Genesis Plus GX Sega Genesis/Megadrive/32X/SegaCD/MegaCD/SMS/GG Emulator for XBox v1.04b Madmab Ed

* Updated to madmab edition interface CFv1b21. See "Interface Changelog.txt"

* Due to an improperly sized array the flicker filter level was resetting to 0 on game load.  Fixed.

* Enabled rewind for GX core.

* Missed some initialization code for cheat searches.
