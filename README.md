# Decked Out 2 Manual Randomizer Guide

## What is Decked Out 2, anyway?

It's a Roguelike built entirely in survival minecraft. Check out [this video](https://youtu.be/aoVVCwx6k1w) to learn more.

## What does randomization do to this game?

There are cards that help you stay alive in the dungeon for longer, and these are randomized.

If you obtain an item, get it from the row of Shulker Boxes in the foyer, and what you do with it depends on what it is:
- If it is a Non-Ethereal card, you can put it into your deck before you start a run, but make sure there's only 40 cards in your deck at maximum. You can use the helpful Card Counter to make sure it's within limits! You can store the unused ones in your Ender Chest (though please throw out the cards that start in your ender chest).
- If it is an Ethereal card, but *not* a Stumble card, you can put it into your deck when you please (or just put it in storage), but it will be consumed on use, so plan when you use them!
- If it is a Stumble (a trap), you *must* put it into your deck in your next run, and if you already have 40 cards, some of them will have to be temporarily removed. Just, please still try in spite of having a very clear temporary disadvantage.
- If it is a Key, you can enter the dungeon with it in your inventory, but like Ethereal cards, they will be consumed, so use them wisely.

## Locations

All locations are toggleable by yaml options, and some can be adjusted to have 0-6 of those locations. 0 removes the locations entirely, and each number after 1 adds a duplicate of each location.

The locations are for:
- Having an amount of Frost Embers when you finish a run
  - This includes the embers from your artifact and the embers from unlocking floors. Once you open up the Frost Ember Shop, it's this amount.
  - If you have more than the amount a location specifies, you can check off that location off as well.
- Having an amount of Coins/Crowns when you finish a run
  - If you have more than the amount a location specifies, you can check off that location off as well.
- Beating runs and obtaining artifacts on certain difficulties
- Getting to places and doing tasks in the 5 levels
- Entering various areas (and doing certain tasks in some of them)
- Purchases in the Crown Shop or Ember Shop
  - You don't need to wait for the right thing to show up so that you can purchase it. Just put the required embers or crowns in the shulker box, and you can mark off the location.
  - If the thing is there to purchase, throw away the thing you get from it. It's supposed to be randomized.
  - You can also buy more Ethereal cards and Crown Shop items after you get their locations and keep them for later use (so that you have *something* to do with spare crowns and embers). Just don't keep any cards that aren't Ethereal.
  - You can enable and disable the ember shop checks as you see fit. I highly recommend turning off legendary cards. They suck.

## Some random notes

- Throw away everything that's in your ender chest by default.
- The pancake that spawns at the start of each run is for making sure you're topped off on food at the start of the run, not for bringing into the dungeon.
- The game doesn't start if you have an empty deck, and breaks if you have a deck with only Ethereal cards. If you have no cards, put a Sneak into your deck, temporarily, until you get any non-Ethereal cards. It should happen relatively quickly, unless you're playing in a really cursed async.

## What is the goal of a Manual game when randomized?

There are 12 goal options to choose from:

- Enter The Hideout:
  - The goal is to make it down to **The Burning Dark** (Level 4), obtain **The Bomb** that spawns in the towers around the level, and bring it to the giant gateway, and put it in the barrel, go in, and push the button to open **The Hideout**, and, in the same run, you need to have obtained a **The Master's Key** artifact from Level 4 (Deepfrost difficulty). Once you've done both of those things, go to the flat structure nearby the gateway, and quickly run through the gap in the side of it (across the pressuren plate), while burning on the magma blocks. There should be a hole to fall down (if there's too small a gap to fit through, you weren't fast enough), and from there you put the master's key into the barrel, and proceed into the hideout. Once you've done that, you've won!
  - It's really hard and luck-based, so be warned!

- Complete a 30/40/50/60/70/80 Ember Run
  - As you enter the Frost Ember Shop, have the required amount of Frost Embers in hand.
  - These are less involved goals, but the early ones have a lot less interesting logic.
  - I think it's cooler to do Enter The Hideout, but like, it is extremely involved, so I get not wanting to do those things.

- Complete 80 Ember and 20 Crown Run
  - Just a bit harder than the 80 ember goal. You need 20 crowns as well!

- Complete a Deepfrost Difficulty run
  - Go down to the Burning Dark, get an artifact, and escape alive on Deepfrost difficulty.

- Blow up the Gateway with the Bomb:
  - An easier form of the hideout goal. No longer requires enough luck to get The Master's Key in the same run you get the bomb.

## Required Software

- Minecraft Java Edition from the [Minecraft Java Edition Store Page](https://www.minecraft.net/en-us/store/minecraft-java-edition)
  - You don't need to have it installed, you just need to own it.
- Archipelago from the [Archipelago Releases Page](https://github.com/ArchipelagoMW/Archipelago/releases)
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
Drop the "Decked Out Expansion Pack 2.0 AP version" folder from world.zip in the [releases](https://github.com/empathy-mp3/decked-out-2-AP/releases/latest) into your saves folder in your Minecraft install.

## Joining a MultiWorld Game

1. Launch the launcher.
2. Click on Manual client on the right.
3. At the top enter your server's ip with the port provided (by default archipelago.gg:38281).
4. In Manual Game ID put "Manual_DeckedOut2_mp3" then press the Connect button on the top right.
5. In the command field at the bottom enter the name of your slot you chose in your Player.yaml then press enter

## Multiplayer

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
- Click the buttons associated with the locations you get in-game on the Manual Client.

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