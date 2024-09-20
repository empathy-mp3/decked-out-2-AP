# Decked Out 2 Manual Randomizer Guide

## What is Decked Out 2, anyway?

It's a Roguelike built entirely in survival minecraft. Check out [this video](https://youtu.be/aoVVCwx6k1w) to learn more.

## Where is the settings page?

The .yaml file is included with the GitHub release.

## What does randomization do to this game?

There are cards that help you stay alive in the dungeon for longer, and these are randomized. There are 6 locations corresponding to each card in the Frost Ember shop at the end of each run, and 5 or 6 locations corresponding to everything you can buy at the Crown Shop in the foyer. Once you buy something, check off all 6 corresponding locations, and throw away whatever it was you purchased.

You can also buy more Ethereal cards and Crown Shop items after you get their locations (so that you have *something* to do with spare crowns and embers). Just don't keep any cards that aren't Ethereal.

If you obtain an item, go into the Master Dungeon Locker on the far back of the foyer, and what you do with it depends on what it is:
- If it is a Non-Ethereal card, you can put it into your deck before you start a run, but make sure there's only 40 cards in your deck at maximum. You can use the helpful Card Counter to make sure it's within limits! You can store the unused ones in your Ender Chest (though please throw out the cards that start in your ender chest).
- If it is an Ethereal card, but *not* a Stumble card, you can put it into your deck when you please (or just put it in storage), but it will be consumed on use, so plan when you use them!
- If it is a Stumble (a trap), you *must* put it into your deck in your next run, and if you already have 40 cards, some of them will have to be temporarily removed. Just, please still try in spite of having a very clear temporary disadvantage
- If it is a Key, you can enter the dungeon with it in your inventory, but like Ethereal cards, they will be consumed, so use them wisely.

## Some random notes

- Get rid of everything that's in your ender chest by default.
- The pancake that spawns at the start of each run is for making sure you're topped off on food at the start of the run, not for bringing into the dungeon.
- The game doesn't start if you have an empty deck, and breaks if you have a deck with only Ethereal cards. If you have no cards, put a Sneak into your deck, temporarily, until you get any non-Ethereal cards. It should happen relatively quickly, unless you're playing in a really cursed async.

## What is the goal of a Manual game when randomized?

There are 7 goal options to choose from:

- Enter The Hideout:
  - The goal is to make it down to **The Burning Dark** (Level 4), obtain **The Bomb** that spawns in the towers around the level, and bring it to the giant gateway, and put it in the barrel, go in, and push the button to open **The Hideout**, and, in the same run, you need to have obtained a **The Master's Key** artifact from Level 4 (Deepfrost difficulty). Once you've done both of those things, go to the flat structure nearby the gateway, and quickly run through the gap in the side of it (across the pressuren plate), while burning on the magma blocks. There should be a hole to fall down (if there's too small a gap to fit through, you weren't fast enough), and from there you put the master's key into the barrel, and proceed into the hideout. Once you've done that, you've won!
  - It's really hard and luck-based, so be warned!

- Craft All Legendary Cards
  - As described further down, go to The Forge, and craft each legendary card.
  - It's a very long goal. Even when you're logically able to get there, you'll have to make 7 separate runs to craft each legendary card (unless you somehow manage to craft multiple legendary cards in one run, which is probably impossible)

- Complete a 30/40/50/60/70 Ember Run
  - As you enter the Frost Ember Shop, have the required amount of Frost Embers in hand.
  - These are less involved goals, but the early ones have a lot less interesting logic.
  - I think it's cooler to do the previous two goals, but like, they are extremely involved, so I get not wanting to do those things.
  - 30 embers *might* be sync-viable, but given how exhausting this game can be (at least to me), it may be better to do this in an async anyway. Perhaps I'm unique in that regard.

## Which items can be in another player's world?

Cards and Keys.

## Required Software

- Minecraft Java Edition from the [Minecraft Java Edition Store Page](https://www.minecraft.net/en-us/store/minecraft-java-edition)
  - You don't need to have it installed, you just need to own it.
- Archipelago from the [Archipelago Releases Page](https://github.com/ArchipelagoMW/Archipelago/releases)
- The [Decked Out Expansion Pack 2.0](https://www.curseforge.com/minecraft/worlds/decked-out-expansion-pack/files/)
- The following mods:

  - [AudioPlayer](https://modrinth.com/mod/audioplayer/version/fabric-1.20.1-1.8.6)
  - [Carpet](https://modrinth.com/mod/carpet/version/1.4.112)
  - [Fabric API](https://modrinth.com/mod/fabric-api/version/0.91.0+1.20.1)
  - [VoiceChat](https://modrinth.com/plugin/simple-voice-chat/version/fabric-1.20.1-2.4.32)

- It's also recommended that you use these (for better optimizations):

  - [Lithium](https://modrinth.com/mod/lithium/version/mc1.20.1-0.11.2) if you're doing this singleplayer
  - [Sodium](https://modrinth.com/mod/sodium/version/mc1.20.1-0.5.3)

## Installation Procedures

Make sure a copy of the Manual world is in the lib/world directory of your client-side installation.
In the Mod Manager of your choice, install all of the mods for Fabric 1.20.1.
Drop the Decked Out Expansion Pack into your saves folder in your Minecraft install.

## Joining a MultiWorld Game

1. Launch the launcher.
2. Click on Manual client on the right.
3. At the top enter your server's ip with the port provided (by default archipelago.gg:38281).
4. In Manual Game ID put "Manual_DeckedOut2_mp3" then press the Connect button on the top right.
5. In the command field at the bottom enter the name of your slot you chose in your Player.yaml then press enter

## Manual Client

In the "Tracker and Locations" tab you'll find buttons corresponding with all the available locations in the Randomizer. Since this is a manual game its built on trust™ you press the locations when you get to them, hopefully in the future only what you can access will be visible but at the moment you could press victory and it would accept it.

## Multiplayer Manual

You can play this with other players (if you use the Decked Out 2 Modpack).
You'll need to host a fabric server, explained in [This Guide](https://fabricmc.net/wiki/player:tutorials:server:windows).
You'll also need to install the following mods onto the server (mostly the same mods as earlier):

- [AudioPlayer](https://modrinth.com/mod/audioplayer/version/fabric-1.20.1-1.8.6)
- [Carpet](https://modrinth.com/mod/carpet/version/1.4.112)
- [Fabric API](https://modrinth.com/mod/fabric-api/version/0.91.0+1.20.1)
- [VoiceChat](https://modrinth.com/plugin/simple-voice-chat/version/fabric-1.20.1-2.4.32)
  
Also, you can install [Lithium](https://modrinth.com/mod/lithium/version/mc1.20.1-0.11.2) for better server optimizations.

- You'll also need to give the resources.zip file that comes with the world download to everyone who joins the server, including yourself.
- After that, go get the Dungeon Lackey item from the Dungeon Master Locker (make sure to make more copies in creative mode), and put one into where it's indicated (*before* putting in the deck).
- I recommend you also go into creative mode and put a chest with several copies of the map you get at the start.
- If you have 3 or more players, you should have a command block set up that says "/tp @p -620 50 1950" so the third and fourth etc. players can join runs.
- However, more players than 2 does make it more difficult.

## Main Game

- Launch your modded install
- Open the Decked Out Expansion Pack
- Obtain a Shulker Box (your deck), put all of the cards you've received thus far into your deck (except for Ethereal cards, which you can save for later), and put a Frozen Shard into the barrel next to the dungeon entrance. 
  - Note: The game doesn't start if you have an empty deck, and breaks if you have a deck with only Ethereal cards. If you have no cards, put a Sneak into your deck, temporarily, until you get any non-Ethereal cards.

## how do i get legendary card locations?

- firstly, you need to find the "warden's office" on either level 3 and pick up a key there. there's a black market near the boat that requires some parkour to get to, and you can use the key to open it up.
- you'll be able to acquire templates for the legendary cards, which you can use, along with the 3 ingredients they list, at the forge in the back of the frost ember shop (which can be opened up for 40 embers).

the methods to obtain those ingredients are as follows:

- melon: hidden button on boat
- glow ink sac: lake/flooded depths (you're allowed to kill glow squids)
- tropical fish: lake/flooded depths (you're allowed to kill tropical fish)
- basalt: burning dark entrance (from black mines)
- spider eye: spider cave (in caves of carnage) (you're allowed to kill them)
- sugar: caves of carnage. button on the back of the axolotl pond
- slimeball: black mines (you're allowed to kill them)
- sweet berry: anywhere
- cactus: use a trapdoor to crouch into a secret area in pearl's desert room in caves of carnage. there's a button
- egg: rusty room (caves of carnage). you have to do parkour
- bone meal: lake/flooded depths (you're allowed to kill tropical fish)
- twisted vine: burning dark. there's a button in a very secluded corner next to the area with a lot of vines
- glow berry: use bone meal on the cave vines near the boat and then harvest those glow berries, but not preexisting ones
- pumpkin: caves of carnage: halloween house (secret button at the back of the house)
- amethyst: caves of carnage (you're allowed to break the amethyst on the budding amethyst blocks)