#! /usr/bin/env python
#! coding=utf-8

# Constants: Races
RACES = ['terran', 'protoss', 'zerg']

# Constants: Unit Lists
TERRAN_UNITS = [
    'scv',
    'mule',
    'marine',
    'marauder',
    'reaper',
    'ghost',
    'hellion',
    'siege_tank',
    'thor',
    'viking',
    'medivac',
    'raven',
    'banshee',
    'battlecruiser',
    'auto_turrent',
    'point_defense_drone',
    'hellbat',
    'widow_mine'
]
PROTOSS_UNITS = [
]
ZERG_UNITS = [
]

# Constants: Terran Units and Structs
_SCV = {
    '_uniq': 'scv',
    '_pict': 'scv.png',
    '_name': 'SCV',
    '_desc': 'Basic worker unit. Can gather resources, build Terran '
             'structures, and repair.',
    '_abil': {
        '01': {
            '_pict': 'terran_repair.jpg',
            '_name': 'Repair',
            '_desc': 'Restores life to mechanical units and structures at the '
                     'cost of resources.',
            '01': 'Hotkey: R'
        },
        '02': {
            '_pict': 'terran_gather.jpg',
            '_name': 'Gather',
            '_desc': 'Orders SCV to gather resources from a selected Mineral '
                     'Field or Vespene Geyser.',
            '01': 'Hotkey: G'
        }
    },
    '_upgd': {
        '01': {
            '_pict': 'terran_infantry_armor_lvl_1.jpg',
            '_name': 'Terran Infantry Armor Level 1',
            '_desc': 'Upgrades the armor of infantry units.',
            '01': 'Hotkey: A',
            '02': 'Research From: Engineering Bay',
            '03': 'Cost: Minerals 100, Gas 100, Time 160'
        },
        '02': {
            '_pict': 'terran_infantry_armor_lvl_2.jpg',
            '_name': 'Terran Infantry Armor Level 2',
            '_desc': 'Further upgrades the armor of infantry units.',
            '01': 'Hotkey: A',
            '02': 'Research From: Engineering Bay',
            '03': 'Cost: Minerals 175, Gas 175, Time 190',
            '04': 'Requires: Armory'
        },
        '03': {
            '_pict': 'terran_infantry_armor_lvl_3.jpg',
            '_name': 'Terran Infantry Armor Level 3',
            '_desc': 'Maximizes the armor of infantry units.',
            '01': 'Hotkey: A',
            '02': 'Research From: Engineering Bay',
            '03': 'Cost: Minerals 250, Gas 250, Time 220',
            '04': 'Requires: Armory'
        }
    },
    '01': 'Race: Terran',
    '02': 'Type: Ground Unit',
    '03': 'Built From: Command Center',
    '04': 'Cost: Minerals 50, Gas 0, Time 17, Supply 1',
    '05': 'Attributes: Biological, Light, Mechanical',
    '06': 'Ground Attack: 5',
    '07': 'Ground DPS: 3.3',
    '08': 'Attack Range: 0.1',
    '09': 'Attack Cooldown: 1.5',
    '10': 'Life: 45',
    '11': 'Armor: 0(+1)',
    '12': 'Hotkey: S',
    '13': 'Sight: 8',
    '14': 'Speed: 2.8125',
    '15': 'Cargo Size: 1'
}
_MULE = {
    '_uniq': 'mule',
    '_pict': 'mule.png',
    '_name': 'MULE',
    '_desc': 'Prototype harvesting unit. Gathers minerals more quickly than '
             'regular SCVs. MULEs last 90 seconds before their systems fail.',
    '_abil': {
        '01': {
            '_pict': 'terran_repair.jpg',
            '_name': 'Repair',
            '_desc': 'Restores life to mechanical units and structures at the '
                     'cost of resources.',
            '01': 'Hotkey: R'
        },
        '02': {
            '_pict': 'terran_gather.jpg',
            '_name': 'Gather',
            '_desc': 'Orders MULE to gather resources from a selected Mineral '
                     'Field.',
            '01': 'Hotkey: G'
        }
    },
    '01': 'Race: Terran',
    '02': 'Type: Ground Unit',
    '03': 'Attributes: Light, Mechanical',
    '04': 'Life: 60',
    '05': 'Armor: 0(+1)',
    '06': 'Hotkey: E',
    '07': 'Sight: 8',
    '08': 'Speed: 2.8125'
}
_MARINE = {
    '_uniq': 'marine',
    '_pict': 'marine.png',
    '_name': 'Marine',
    '_desc': 'General-purpose infantry.',
    '_abil': {
        '01': {
            '_pict': 'terran_stimpack.jpg',
            '_name': 'Use Stimpack',
            '_desc': 'Increases the movement speed and firing rate by 50% at '
                     'the cost of 10 HP for a Marine or 20 HP for a Marauder.',
            '01': 'Hotkey: T',
            '02': 'Range: Self',
            '03': 'Duration: 15 seconds'
        }
    },
    '_upgd': {
        '01': {
            '_pict': 'terran_infantry_armor_lvl_1.jpg',
            '_name': 'Terran Infantry Armor Level 1',
            '_desc': 'Upgrades the armor of infantry units.',
            '01': 'Hotkey: A',
            '02': 'Research From: Engineering Bay',
            '03': 'Cost: Minerals 100, Gas 100, Time 160'
        },
        '02': {
            '_pict': 'terran_infantry_armor_lvl_2.jpg',
            '_name': 'Terran Infantry Armor Level 2',
            '_desc': 'Further upgrades the armor of infantry units.',
            '01': 'Hotkey: A',
            '02': 'Research From: Engineering Bay',
            '03': 'Cost: Minerals 175, Gas 175, Time 190',
            '04': 'Requires: Armory'
        },
        '03': {
            '_pict': 'terran_infantry_armor_lvl_3.jpg',
            '_name': 'Terran Infantry Armor Level 3',
            '_desc': 'Maximizes the armor of infantry units.',
            '01': 'Hotkey: A',
            '02': 'Research From: Engineering Bay',
            '03': 'Cost: Minerals 250, Gas 250, Time 220',
            '04': 'Requires: Armory'
        },
        '04': {
            '_pict': 'terran_infantry_weapons_lvl_1.jpg',
            '_name': 'Terran Infantry Weapons Level 1',
            '_desc': 'Upgrades the damage dealt by infantry units.',
            '01': 'Hotkey: E',
            '02': 'Research From: Engineering Bay',
            '03': 'Cost: Minerals 100, Gas 100, Time 160'
        },
        '05': {
            '_pict': 'terran_infantry_weapons_lvl_2.jpg',
            '_name': 'Terran Infantry Weapons Level 2',
            '_desc': 'Further upgrades the damage dealt by infantry units.',
            '01': 'Hotkey: E',
            '02': 'Research From: Engineering Bay',
            '03': 'Cost: Minerals 175, Gas 175, Time 190',
            '04': 'Requires: Armory'
        },
        '06': {
            '_pict': 'terran_infantry_weapons_lvl_3.jpg',
            '_name': 'Terran Infantry Weapons Level 3',
            '_desc': 'Maximizes the damage dealt by infantry units.',
            '01': 'Hotkey: E',
            '02': 'Research From: Engineering Bay',
            '03': 'Cost: Minerals 250, Gas 250, Time 220',
            '04': 'Requires: Armory'
        },
        '07': {
            '_pict': 'terran_stimpack.jpg',
            '_name': 'Stimpack',
            '_desc': 'Enables Marines and Marauders to use the Stimpack '
                     'ability. Stimpacks cause damage to a unit, but they '
                     'increase its attack and movement speeds for a short '
                     'time.',
            '01': 'Hotkey: T',
            '02': 'Research From: Tech Lab (Attached to Barracks)',
            '03': 'Cost: Minerals 100, Gas 100, Time 170'
        },
        '08': {
            '_pict': 'terran_combat_shield.jpg',
            '_name': 'Combat Shield',
            '_desc': 'Marines gain +10 life.',
            '01': 'Hotkey: C',
            '02': 'Research From: Tech Lab (Attached to Barracks)',
            '03': 'Cost: Minerals 100, Gas 100, Time 110'
        }
    },
    '01': 'Race: Terran',
    '02': 'Type: Ground Unit',
    '03': 'Built From: Barracks',
    '04': 'Cost: Minerals 50, Gas 0, Time 25, Supply 1',
    '05': 'Attributes: Biological, Light',
    '06': 'Ground Attack: 6(+1)',
    '07': 'Ground DPS: 7(+1.2)',
    '08': 'Ground DPS with Stimpack: 10.5(+1.7)',
    '09': 'Air Attack: 6(+1)',
    '10': 'Air DPS: 7(+1.2)',
    '11': 'Air DPS with Stimpack: 10.5(+1.7)',
    '12': 'Attack Range: 5',
    '13': 'Attack Cooldown: 0.8608',
    '14': 'Attack Cooldown with Stimpack: 0.5739',
    '15': 'Life: 45',
    '16': 'Life with Combat Shield: 55',
    '17': 'Armor: 0(+1)',
    '18': 'Hotkey: A',
    '19': 'Sight: 9',
    '20': 'Speed: 2.25',
    '21': 'Speed with Stimpack: 3.375',
    '22': 'Cargo Size: 1'
}
_MARAUDER = {
    '_uniq': 'marauder',
    '_pict': 'marauder.png',
    '_name': 'Marauder',
    '_desc': 'Heavy assault infantry.',
    '_abil': {
        '01': {
            '_pict': 'terran_stimpack.jpg',
            '_name': 'Use Stimpack',
            '_desc': 'Increases the movement speed and firing rate by 50% at '
                     'the cost of 10 HP for a Marine or 20 HP for a Marauder.',
            '01': 'Hotkey: T',
            '02': 'Range: Self',
            '03': 'Duration: 15 seconds'
        },
        '02': {
            '_pict': 'terran_concussive_shells.jpg',
            '_name': 'Concussive Shells',
            '_desc': 'Slows an enemy\'s movement speed by 50% when hit by the '
                     'Marauder\'s attack. The slowing effect does not stack, '
                     'but the timer is refreshed by subsequent hits. Massive '
                     'units are immune to the slow.',
            '01': 'Duration: 1.5 seconds'
        }
    },
    '_upgd': {
        '01': {
            '_pict': 'terran_infantry_armor_lvl_1.jpg',
            '_name': 'Terran Infantry Armor Level 1',
            '_desc': 'Upgrades the armor of infantry units.',
            '01': 'Hotkey: A',
            '02': 'Research From: Engineering Bay',
            '03': 'Cost: Minerals 100, Gas 100, Time 160'
        },
        '02': {
            '_pict': 'terran_infantry_armor_lvl_2.jpg',
            '_name': 'Terran Infantry Armor Level 2',
            '_desc': 'Further upgrades the armor of infantry units.',
            '01': 'Hotkey: A',
            '02': 'Research From: Engineering Bay',
            '03': 'Cost: Minerals 175, Gas 175, Time 190',
            '04': 'Requires: Armory'
        },
        '03': {
            '_pict': 'terran_infantry_armor_lvl_3.jpg',
            '_name': 'Terran Infantry Armor Level 3',
            '_desc': 'Maximizes the armor of infantry units.',
            '01': 'Hotkey: A',
            '02': 'Research From: Engineering Bay',
            '03': 'Cost: Minerals 250, Gas 250, Time 220',
            '04': 'Requires: Armory'
        },
        '04': {
            '_pict': 'terran_infantry_weapons_lvl_1.jpg',
            '_name': 'Terran Infantry Weapons Level 1',
            '_desc': 'Upgrades the damage dealt by infantry units.',
            '01': 'Hotkey: E',
            '02': 'Research From: Engineering Bay',
            '03': 'Cost: Minerals 100, Gas 100, Time 160'
        },
        '05': {
            '_pict': 'terran_infantry_weapons_lvl_2.jpg',
            '_name': 'Terran Infantry Weapons Level 2',
            '_desc': 'Further upgrades the damage dealt by infantry units.',
            '01': 'Hotkey: E',
            '02': 'Research From: Engineering Bay',
            '03': 'Cost: Minerals 175, Gas 175, Time 190',
            '04': 'Requires: Armory'
        },
        '06': {
            '_pict': 'terran_infantry_weapons_lvl_3.jpg',
            '_name': 'Terran Infantry Weapons Level 3',
            '_desc': 'Maximizes the damage dealt by infantry units.',
            '01': 'Hotkey: E',
            '02': 'Research From: Engineering Bay',
            '03': 'Cost: Minerals 250, Gas 250, Time 220',
            '04': 'Requires: Armory'
        },
        '07': {
            '_pict': 'terran_stimpack.jpg',
            '_name': 'Stimpack',
            '_desc': 'Enables Marines and Marauders to use the Stimpack '
                     'ability. Stimpacks cause damage to a unit, but they '
                     'increase its attack and movement speeds for a short '
                     'time.',
            '01': 'Hotkey: T',
            '02': 'Research From: Tech Lab (Attached to Barracks)',
            '03': 'Cost: Minerals 100, Gas 100, Time 170'
        },
        '08': {
            '_pict': 'terran_concussive_shells.jpg',
            '_name': 'Concussive Shells',
            '_desc': 'Marauders gain the Concussive Shells ability.',
            '01': 'Research From: Tech Lab (Attached to Barracks)',
            '02': 'Cost: Minerals 50, Gas 50, Time 60'
        }
    },
    '01': 'Race: Terran',
    '02': 'Type: Ground Unit',
    '03': 'Built From: Barracks',
    '04': 'Cost: Minerals 100, Gas 25, Time 30, Supply 2',
    '05': 'Attributes: Armored, Biological',
    '06': 'Ground Attack: 10(+1)',
    '07': 'Ground Attack vs. Armored: 20(+2)',
    '08': 'Ground DPS: 6.7(+0.7)',
    '09': 'Ground DPS vs. Armored: 13.4(+1.4)',
    '10': 'Ground DPS After Stimpack: 10(+1)',
    '11': 'Ground DPS vs. Armored After Stimpack: 20(+2)',
    '12': 'Attack Range: 6',
    '13': 'Attack Cooldown: 1.5',
    '14': 'Attack Cooldown After Stimpack: 1',
    '15': 'Life: 125',
    '16': 'Armor: 1(+1)',
    '17': 'Hotkey: D',
    '18': 'Sight: 10',
    '19': 'Speed: 2.25',
    '20': 'Speed After Stimpack: 3.375',
    '21': 'Cargo Size: 2'
}
_REAPER = {
    '_uniq': 'reaper',
    '_pict': 'reaper.png',
    '_name': 'Reaper',
    '_desc': 'Raider. Capable of jumping up and down cliffs. Heals when out '
             'of combat.',
    '_abil': {
        '01': {
            '_pict': 'terran_jet_pack.jpg',
            '_name': 'Jet Pack',
            '_desc': 'Allows Reapers to travel up and down cliffs.'
        },
        '02': {
            '_pict': 'terran_combat_drugs.jpg',
            '_name': 'Combat Drugs',
            '_desc': 'Heals 2 HP every second if the Reaper is not attacked '
                     'for 10 seconds'
        }
    },
    '_upgd': {
        '01': {
            '_pict': 'terran_infantry_armor_lvl_1.jpg',
            '_name': 'Terran Infantry Armor Level 1',
            '_desc': 'Upgrades the armor of infantry units.',
            '01': 'Hotkey: A',
            '02': 'Reseach From: Engineering Bay',
            '03': 'Cost: Minerals 100, Gas 100, Time 160'
        },
        '02': {
            '_pict': 'terran_infantry_armor_lvl_2.jpg',
            '_name': 'Terran Infantry Armor Level 2',
            '_desc': 'Further upgrades the armor of infantry units.',
            '01': 'Hotkey: A',
            '02': 'Research From: Engineering Bay',
            '03': 'Cost: Minerals 175, Gas 175, Time 190',
            '04': 'Requires: Armory'
        },
        '03': {
            '_pict': 'terran_infantry_armor_lvl_3.jpg',
            '_name': 'Terran Infantry Armor Level 3',
            '_desc': 'Maximizes the armor of infantry units.',
            '01': 'Hotkey: A',
            '02': 'Research From: Engineering Bay',
            '03': 'Cost: Minerals 250, Gas 250, Time 220',
            '04': 'Rquires: Armory'
        },
        '04': {
            '_pict': 'terran_infantry_weapons_lvl_1.jpg',
            '_name': 'Terran Infantry Weapons Level 1',
            '_desc': 'Upgrades the damage dealt by infantry units.',
            '01': 'Hotkey: E',
            '02': 'Research From: Engineering Bay',
            '03': 'Cost: Minerals 100, Gas 100, Time 160'
        },
        '05': {
            '_pict': 'terran_infantry_weapons_lvl_2.jpg',
            '_name': 'Terran Infantry Weapons Level 2',
            '_desc': 'Further upgrades the damage dealt by infantry units.',
            '01': 'Hotkey: E',
            '02': 'Research From: Engineering Bay',
            '03': 'Cost: Minerals 175, Gas 175, Time 190',
            '04': 'Requires: Armory'
        },
        '06': {
            '_pict': 'terran_infantry_weapons_lvl_3.jpg',
            '_name': 'Terran Infantry Weapons Level 3',
            '_desc': 'Maximizes the damage dealt by infantry units.',
            '01': 'Hotkey: E',
            '02': 'Research From: Engineering Bay',
            '03': 'Cost: Minerals 250, Gas 250, Time 220',
            '04': 'Requires: Armory'
        }
    },
    '01': 'Race: Terran',
    '02': 'Type: Ground Unit',
    '03': 'Built From: Barracks',
    '04': 'Cost: Minerals 50, Gas 50, Time 45, Supply 1',
    '05': 'Attributes: Biological, Light',
    '06': 'Ground Attack: 4(+1)*2',
    '07': 'Ground DPS: 7.3(+1.8)',
    '08': 'Attack Range: 5',
    '09': 'Attack Cooldown: 1.1',
    '10': 'Life: 60',
    '11': 'Armor: 0(+1)',
    '12': 'Hotkey: R',
    '13': 'Sight: 9',
    '14': 'Speed: 3.75',
    '15': 'Cargo Size: 1'
}
_GHOST = {
    '_uniq': 'ghost',
    '_pict': 'ghost.png',
    '_name': 'Ghost',
    '_desc': 'Sniper. Can use Snipe, EMP Round and Cloak. Can call down Nukes '
             'built at the Ghost Academy.',
    '_abil': {
        '01': {
            '_pict': 'terran_sniper_round.jpg',
            '_name': 'Sniper Round',
            '_desc': 'The Ghost snipes a single, biological unit for 25 '
                     '(+25 vs. psionic) damage. This ability can be queued '
                     'for multiple snipes',
            '01': 'Hotkey: R',
            '02': 'Cost: Energy 25',
            '03': 'Range: 10',
            '04': 'Duration: 0.5 second'
        },
        '02': {
            '_pict': 'terran_emp_round.jpg',
            '_name': 'EMP Round',
            '_desc': 'The Ghost fires an EMP Round that removes up to 100 '
                     'shields and energy from every unit within the AoE. '
                     'Also reveals cloaked units.',
            '01': 'Hotkey: E',
            '02': 'Cost: Energy 75',
            '03': 'Range: 10',
            '04': 'Radius: 1.5'
        },
        '03': {
            '_pict': 'terran_cloak.jpg',
            '_name': 'Cloak',
            '_desc': 'The Ghost becomes invisible until it runs out of '
                     'energy or the player cancels Cloak.',
            '01': 'Hotkey: C',
            '02': 'Cost: Energy 25, then 0.9/second'
        },
        '04': {
            '_pict': 'terran_tac_nuke_strike.jpg',
            '_name': 'Tac Nuke Strike',
            '_desc': 'The Ghost calls down a nuclear strike at the targeted '
                     'spot. Nukes take 20 seconds to land.',
            '01': 'Hotkey: N',
            '02': 'Range: 12',
            '03': 'Cooldown: 20 seconds',
            '04': 'Damage: 300(+200 vs. buildings)'
        },
    },
    '_upgd': {
        '01': {
            '_pict': 'terran_infantry_armor_lvl_1.jpg',
            '_name': 'Terran Infantry Armor Level 1',
            '_desc': 'Upgrades the armor of infantry units.',
            '01': 'Hotkey: A',
            '02': 'Reseach From: Engineering Bay',
            '03': 'Cost: Minerals 100, Gas 100, Time 160'
        },
        '02': {
            '_pict': 'terran_infantry_armor_lvl_2.jpg',
            '_name': 'Terran Infantry Armor Level 2',
            '_desc': 'Further upgrades the armor of infantry units.',
            '01': 'Hotkey: A',
            '02': 'Research From: Engineering Bay',
            '03': 'Cost: Minerals 175, Gas 175, Time 190',
            '04': 'Requires: Armory'
        },
        '03': {
            '_pict': 'terran_infantry_armor_lvl_3.jpg',
            '_name': 'Terran Infantry Armor Level 3',
            '_desc': 'Maximizes the armor of infantry units.',
            '01': 'Hotkey: A',
            '02': 'Research From: Engineering Bay',
            '03': 'Cost: Minerals 250, Gas 250, Time 220',
            '04': 'Rquires: Armory'
        },
        '04': {
            '_pict': 'terran_infantry_weapons_lvl_1.jpg',
            '_name': 'Terran Infantry Weapons Level 1',
            '_desc': 'Upgrades the damage dealt by infantry units.',
            '01': 'Hotkey: E',
            '02': 'Research From: Engineering Bay',
            '03': 'Cost: Minerals 100, Gas 100, Time 160'
        },
        '05': {
            '_pict': 'terran_infantry_weapons_lvl_2.jpg',
            '_name': 'Terran Infantry Weapons Level 2',
            '_desc': 'Further upgrades the damage dealt by infantry units.',
            '01': 'Hotkey: E',
            '02': 'Research From: Engineering Bay',
            '03': 'Cost: Minerals 175, Gas 175, Time 190',
            '04': 'Requires: Armory'
        },
        '06': {
            '_pict': 'terran_infantry_weapons_lvl_3.jpg',
            '_name': 'Terran Infantry Weapons Level 3',
            '_desc': 'Maximizes the damage dealt by infantry units.',
            '01': 'Hotkey: E',
            '02': 'Research From: Engineering Bay',
            '03': 'Cost: Minerals 250, Gas 250, Time 220',
            '04': 'Requires: Armory'
        },
        '07': {
            '_pict': 'terran_cloak.jpg',
            '_name': 'Personal Cloaking',
            '_desc': 'Allows Ghosts to use Cloak ability.',
            '01': 'Hotkey: C',
            '02': 'Research From: Ghost Academy',
            '03': 'Cost: Minerals 150, Gas 150, Time 120'
        },
        '08': {
            '_pict': 'terran_moebius_reactor.jpg',
            '_name': 'Moebius Reactor',
            '_desc': 'Increases the Ghost\'s starting energy by 25.',
            '01': 'Hotkey: M',
            '02': 'Research From: Ghost Academy',
            '03': 'Cost: Minerals 100, Gas 100, Time 80'
        }
    },
    '01': 'Race: Terran',
    '02': 'Type: Ground Unit',
    '03': 'Built From: Barracks',
    '04': 'Cost: Minerals 200, Gas 100, Time 40, Supply 2',
    '05': 'Attributes: Biological, Psionic',
    '06': 'Ground Attack: 10(+1)',
    '07': 'Ground Attack vs. Light: 20(+2)',
    '08': 'Ground DPS: 6.7(+0.7)',
    '09': 'Ground DPS vs. Light: 13.4(+1.4)',
    '10': 'Air Attack: 10(+1)',
    '11': 'Air Attack vs. Light: 20(+2)',
    '12': 'Air DPS: 6.7(+0.7)',
    '13': 'Air DPS vs. Light: 13.4(+1.4)',
    '14': 'Attack Range: 6',
    '15': 'Attack Cooldown: 1.5',
    '16': 'Life: 100',
    '17': 'Armor: 0(+1)',
    '18': 'Hotkey: G',
    '19': 'Energy: 50(+25)/200',
    '20': 'Sight: 11',
    '21': 'Speed: 2.25',
    '22': 'Cargo Size: 2'
}
_HELLION = {
    '_uniq': 'hellion',
    '_pict': 'hellion.png',
    '_name': 'Hellion',
    '_desc': 'Fast scout. Has a flame attack that damages all enemy units '
             'in its line of fire.',
    '_abil': {
        '01': {
            '_pict': 'terran_hellbat_mode.jpg',
            '_name': 'Hellbat Mode',
            '_desc': 'Transforms the Hellion into its Hellbat form. Requires '
                     'the Transformation Servos upgrade.',
            '01': 'Hotkey: D',
            '02': 'Duration: 4 seconds'
        }
    },
    '_upgd': {
        '01': {
            '_pict': 'terran_vehicle_and_ship_plating_lvl_1.jpg',
            '_name': 'Vehicle and Ship Plating Level 1',
            '_desc': 'Upgrades the armor of Terran Factory and Starport '
                     'units.',
            '01': 'Hotkey: E',
            '02': 'Research From: Armory',
            '03': 'Cost: Minerals 100, Gas 100, Time 160'
        },
        '02': {
            '_pict': 'terran_vehicle_and_ship_plating_lvl_2.jpg',
            '_name': 'Vehicle and Ship Plating Level 2',
            '_desc': 'Further upgrades the armor of Terran Factory and '
                     'Starport units.',
            '01': 'Hotkey: E',
            '02': 'Research From: Armory',
            '03': 'Cost: Minerals 175, Gas 175, Time 190'
        },
        '03': {
            '_pict': 'terran_vehicle_and_ship_plating_lvl_3.jpg',
            '_name': 'Vehicle and Ship Plating Level 3',
            '_desc': 'Maximizes the armor of Terran Factory and Starport '
                     'units.',
            '01': 'Hotkey: E',
            '02': 'Research From: Armory',
            '03': 'Cost: Minerals 250, Gas 250, Time 220'
        },
        '04': {
            '_pict': 'terran_vehicle_and_ship_weapons_lvl_1.jpg',
            '_name': 'Vehicle and Ship Weapons Level 1',
            '_desc': 'Upgrades the damage of Terran Factory and Starport '
                     'units.',
            '01': 'Hotkey: V',
            '02': 'Research From: Armory',
            '03': 'Cost: Minerals 100, Gas 100, Time 160'
        },
        '05': {
            '_pict': 'terran_vehicle_and_ship_weapons_lvl_2.jpg',
            '_name': 'Vehicle and Ship Weapons Level 2',
            '_desc': 'Further upgrades the damage of Terran Factory and '
                     'Starport units.',
            '01': 'Hotkey: V',
            '02': 'Research From: Armory',
            '03': 'Cost: Minerals 175, Gas 175, Time 190'
        },
        '06': {
            '_pict': 'terran_vehicle_and_ship_weapons_lvl_3.jpg',
            '_name': 'Vehicle and Ship Weapons Level 3',
            '_desc': 'Maximizes the damage of Terran Factory and Starport '
                     'units.',
            '01': 'Hotkey: V',
            '02': 'Research From: Armory',
            '03': 'Cost: Minerals 175, Gas 175, Time 190'
        },
        '07': {
            '_pict': 'terran_infernal_pre_igniter.jpg',
            '_name': 'Infernal Pre-Igniter',
            '_desc': 'Improves the Hellion\'s bonus against Light units by +5 '
                     'damage and the Hellbat\'s bonus against Light units by '
                     '+12 damage.',
            '01': 'Hotkey: I',
            '02': 'Research From: Tech Lab (Attached to Factory)',
            '03': 'Cost: Minerals 150, Gas 150, Time 110'
        },
        '08': {
            '_pict': 'terran_transformation_servos.jpg',
            '_name': 'Transformation Servos',
            '_desc': 'Allows Hellions and Hellbats to transform between modes '
                     'freely. Requires an Armory.',
            '01': 'Hotkey: T',
            '02': 'Research From: Tech Lab (Attached to Factory)',
            '03': 'Cost: Minerals 150, Gas 150, Time 110'
        }
    },
    '01': 'Race: Terran',
    '02': 'Built From: Factory',
    '03': 'Cost: Minerals 100, Gas 0, Time 30, Supply 2',
    '04': 'Attributes: Light, Mechanical',
    '05': 'Ground Attack: 8(+1)',
    '06': 'Ground Attack vs. Light: 14(+2)',
    '07': 'Ground Attack vs. Light with Infernal Pre-Igniter: 19(+2)',
    '08': 'Ground DPS: 3.2(+0.4)',
    '09': 'Ground DPS vs. Light: 5.6(+0.8)',
    '10': 'Ground DPS vs. Light with Infernal Pre-Igniter: 7.6(+0.8)',
    '11': 'Attack Range: 5',
    '12': 'Attack Cooldown: 2.5',
    '13': 'Life: 90',
    '14': 'Armor: 0(+1)',
    '15': 'Hotkey: E',
    '16': 'Sight: 10',
    '17': 'Speed: 4.25',
    '18': 'Cargo Size: 2'
}
_SIEGE_TANK = {
    '_uniq': 'siege_tank',
    '_pict': 'siege_tank.png',
    '_name': 'Siege Tank',
    '_desc': 'Heavy Tank. Can switch into Siege Mode to provide long range '
             'artillery support.',
    '_abil': {
        '01': {
            '_pict': 'terran_siege_mode.jpg',
            '_name': 'Siege Mode',
            '_desc': 'Transforms the Siege Tank into Siege Mode where it '
                     'gains splash damage, greatly increased range and damage '
                     'at the cost of losing all mobility and a slower firing '
                     'rate.',
            '01': 'Hotkey: E',
            '02': 'Duration: 4 seconds'
        },
        '02': {
            '_pict': 'terran_tank_mode.jpg',
            '_name': 'Tank Mode',
            '_desc': 'Transforms the Siege Tank back into Tank Mode, where it '
                     'gains the ability to move and fire at faster rate.',
            '01': 'Hotkey: D',
            '02': 'Duration: 4 seconds'
        }
    },
    '_upgd': {
        '01': {
            '_pict': 'terran_vehicle_and_ship_plating_lvl_1.jpg',
            '_name': 'Vehicle and Ship Plating Level 1',
            '_desc': 'Upgrades the armor of Terran Factory and Starport '
                     'units.',
            '01': 'Hotkey: E',
            '02': 'Research From: Armory',
            '03': 'Cost: Minerals 100, Gas 100, Time 160'
        },
        '02': {
            '_pict': 'terran_vehicle_and_ship_plating_lvl_2.jpg',
            '_name': 'Vehicle and Ship Plating Level 2',
            '_desc': 'Further upgrades the armor of Terran Factory and '
                     'Starport units.',
            '01': 'Hotkey: E',
            '02': 'Research From: Armory',
            '03': 'Cost: Minerals 175, Gas 175, Time 190'
        },
        '03': {
            '_pict': 'terran_vehicle_and_ship_plating_lvl_3.jpg',
            '_name': 'Vehicle and Ship Plating Level 3',
            '_desc': 'Maximizes the armor of Terran Factory and Starport '
                     'units.',
            '01': 'Hotkey: E',
            '02': 'Research From: Armory',
            '03': 'Cost: Minerals 250, Gas 250, Time 220'
        },
        '04': {
            '_pict': 'terran_vehicle_and_ship_weapons_lvl_1.jpg',
            '_name': 'Vehicle and Ship Weapons Level 1',
            '_desc': 'Upgrades the damage of Terran Factory and Starport '
                     'units.',
            '01': 'Hotkey: V',
            '02': 'Research From: Armory',
            '03': 'Cost: Minerals 100, Gas 100, Time 160'
        },
        '05': {
            '_pict': 'terran_vehicle_and_ship_weapons_lvl_2.jpg',
            '_name': 'Vehicle and Ship Weapons Level 2',
            '_desc': 'Further upgrades the damage of Terran Factory and '
                     'Starport units.',
            '01': 'Hotkey: V',
            '02': 'Research From: Armory',
            '03': 'Cost: Minerals 175, Gas 175, Time 190'
        },
        '06': {
            '_pict': 'terran_vehicle_and_ship_weapons_lvl_3.jpg',
            '_name': 'Vehicle and Ship Weapons Level 3',
            '_desc': 'Maximizes the damage of Terran Factory and Starport '
                     'units.',
            '01': 'Hotkey: V',
            '02': 'Research From: Armory',
            '03': 'Cost: Minerals 175, Gas 175, Time 190'
        }
    },
    '01': 'Race: Terran',
    '02': 'Type: Ground Unit',
    '03': 'Built From: Factory',
    '04': 'Cost: Minerals 150, Gas 125, Time 45, Supply 3',
    '05': 'Attributes: Armored, Mechanical',
    '06': 'Ground Attack in Mobile Mode: 15(+2)',
    '07': 'Ground Attack in Mobile Mode vs. Armored: 25(+3)',
    '08': 'Ground Attack in Siege Mode: 35(+3) (Splash)',
    '09': 'Ground Attack in Siege Mode vs. Armored: 50(+5) (Splash)',
    '10': 'Ground DPS in Mobile Mode: 14.4(+1.9)',
    '11': 'Ground DPS in Mobile Mode vs. Armored: 24(+2.9)',
    '12': 'Ground DPS in Siege Mode: 12.5(+1.1)',
    '13': 'Ground DPS in Siege Mode vs. Armored: 17.9(+1.8)',
    '14': 'Attack Range in Mobile Mode: 7',
    '15': 'Attack Range in Siege Mode: 13',
    '16': 'Attack Cooldown in Mobile Mode: 1.04',
    '17': 'Attack Cooldown in Siege Mode: 2.8',
    '18': 'Life: 160',
    '19': 'Armor: 1(+1)',
    '20': 'Hotkey: S',
    '21': 'Sight: 11',
    '22': 'Speed in Mobile Mode: 2.25',
    '23': 'Speed in Siege Mode: 0',
    '24': 'Cargo Size: 4'
}
_THOR = {
    '_uniq': 'thor',
    '_pict': 'thor.png',
    '_name': 'Thor',
    '_desc': 'Heavy Assault Mech.',
    '_abil': {
        '01': {
            '_pict': 'terran_high_impact_payload.jpg',
            '_name': 'High Impact Payload',
            '_desc': 'Activates the Thor\'s 250mm Punisher Cannons, which '
                     'strike a single air target for heavy damage.',
            '01': 'Hotkey: E',
            '02': 'Duration: 4 seconds'
        },
        '02': {
            '_pict': 'terran_explosive_payload.jpg',
            '_name': 'Explosive Payload',
            '_desc': 'Arms the Thor\'s Javelin missile launchers, which do '
                     'splash damage to air units and additional damage to '
                     'Light units.',
            '01': 'Hotkey: D',
            '02': 'Duration: 4 seconds'
        }
    },
    '_upgd': {
        '01': {
            '_pict': 'terran_vehicle_and_ship_plating_lvl_1.jpg',
            '_name': 'Vehicle and Ship Plating Level 1',
            '_desc': 'Upgrades the armor of Terran Factory and Starport '
                     'units.',
            '01': 'Hotkey: E',
            '02': 'Research From: Armory',
            '03': 'Cost: Minerals 100, Gas 100, Time 160'
        },
        '02': {
            '_pict': 'terran_vehicle_and_ship_plating_lvl_2.jpg',
            '_name': 'Vehicle and Ship Plating Level 2',
            '_desc': 'Further upgrades the armor of Terran Factory and '
                     'Starport units.',
            '01': 'Hotkey: E',
            '02': 'Research From: Armory',
            '03': 'Cost: Minerals 175, Gas 175, Time 190'
        },
        '03': {
            '_pict': 'terran_vehicle_and_ship_plating_lvl_3.jpg',
            '_name': 'Vehicle and Ship Plating Level 3',
            '_desc': 'Maximizes the armor of Terran Factory and Starport '
                     'units.',
            '01': 'Hotkey: E',
            '02': 'Research From: Armory',
            '03': 'Cost: Minerals 250, Gas 250, Time 220'
        },
        '04': {
            '_pict': 'terran_vehicle_and_ship_weapons_lvl_1.jpg',
            '_name': 'Vehicle and Ship Weapons Level 1',
            '_desc': 'Upgrades the damage of Terran Factory and Starport '
                     'units.',
            '01': 'Hotkey: V',
            '02': 'Research From: Armory',
            '03': 'Cost: Minerals 100, Gas 100, Time 160'
        },
        '05': {
            '_pict': 'terran_vehicle_and_ship_weapons_lvl_2.jpg',
            '_name': 'Vehicle and Ship Weapons Level 2',
            '_desc': 'Further upgrades the damage of Terran Factory and '
                     'Starport units.',
            '01': 'Hotkey: V',
            '02': 'Research From: Armory',
            '03': 'Cost: Minerals 175, Gas 175, Time 190'
        },
        '06': {
            '_pict': 'terran_vehicle_and_ship_weapons_lvl_3.jpg',
            '_name': 'Vehicle and Ship Weapons Level 3',
            '_desc': 'Maximizes the damage of Terran Factory and Starport '
                     'units.',
            '01': 'Hotkey: V',
            '02': 'Research From: Armory',
            '03': 'Cost: Minerals 175, Gas 175, Time 190'
        }
    },
    '01': 'Race: Terran',
    '02': 'Type: Ground Unit',
    '03': 'Built From: Factory',
    '04': 'Cost: Minerals 300, Gas 200, Time 60, Supply 6',
    '05': 'Attributes: Armored, Massive, Mechanical',
    '06': 'Ground Attack: 30(+3)*2',
    '07': 'Ground DPS: 46.9(+4.7)',
    '08': 'Air Attack in Explosive Mode: 6(+1)*4 (Splash)',
    '09': 'Air Attack in Explosive Mode vs. Light Air: 12(+2)*4 (Splash)',
    '10': 'Air Attack in High Impact Mode: 24(+2)',
    '11': 'Air DPS in Explosive Mode: 8(+1.3)',
    '12': 'Air DPS in Explosive Mode vs. Light Air: 16(+2.6) (Splash)',
    '13': 'Air DPS in High Impact Mode: 12(+1)',
    '14': 'Ground Attack Range: 7',
    '15': 'Air Attack Range: 10',
    '16': 'Ground Attack Cooldown: 1.28',
    '17': 'Air Attack in Explosive Mode: 3',
    '18': 'Air Attack in High Impact Mode: 2',
    '19': 'Life: 400',
    '20': 'Armor: 1(+1)',
    '21': 'Hotkey: T',
    '22': 'Sight: 11',
    '23': 'Speed: 1.875',
    '24': 'Cargo Size: 8'
}
_VIKING = {
    '_uniq': 'viking',
    '_pict': 'viking.png',
    '_name': 'Viking',
    '_desc': 'Versatile support flyer loaded with strong anti-captial air '
             'missiles. Can switch into Assault mode to attack ground units.',
    '_abil': {
        '01': {
            '_pict': 'terran_fighter_mode.jpg',
            '_name': 'Fighter Mode',
            '_desc': 'Transforms the Viking into Fighter Mode where it '
                     'becomes an Air unit with an anti-air attack.',
            '01': 'Hotkey: E',
            '02': 'Duration: 4 seconds'
        },
        '02': {
            '_pict': 'terran_assault_mode.jpg',
            '_name': 'Assault Mode',
            '_desc': 'Transforms the Viking into Assault Mode where it '
                     'becomes a Ground unit with a ground attack.',
            '01': 'Hotkey: D',
            '02': 'Duration: 4 seconds'
        }
    },
    '_upgd': {
        '01': {
            '_pict': 'terran_vehicle_and_ship_plating_lvl_1.jpg',
            '_name': 'Vehicle and Ship Plating Level 1',
            '_desc': 'Upgrades the armor of Terran Factory and Starport '
                     'units.',
            '01': 'Hotkey: E',
            '02': 'Research From: Armory',
            '03': 'Cost: Minerals 100, Gas 100, Time 160'
        },
        '02': {
            '_pict': 'terran_vehicle_and_ship_plating_lvl_2.jpg',
            '_name': 'Vehicle and Ship Plating Level 2',
            '_desc': 'Further upgrades the armor of Terran Factory and '
                     'Starport units.',
            '01': 'Hotkey: E',
            '02': 'Research From: Armory',
            '03': 'Cost: Minerals 175, Gas 175, Time 190'
        },
        '03': {
            '_pict': 'terran_vehicle_and_ship_plating_lvl_3.jpg',
            '_name': 'Vehicle and Ship Plating Level 3',
            '_desc': 'Maximizes the armor of Terran Factory and Starport '
                     'units.',
            '01': 'Hotkey: E',
            '02': 'Research From: Armory',
            '03': 'Cost: Minerals 250, Gas 250, Time 220'
        },
        '04': {
            '_pict': 'terran_vehicle_and_ship_weapons_lvl_1.jpg',
            '_name': 'Vehicle and Ship Weapons Level 1',
            '_desc': 'Upgrades the damage of Terran Factory and Starport '
                     'units.',
            '01': 'Hotkey: V',
            '02': 'Research From: Armory',
            '03': 'Cost: Minerals 100, Gas 100, Time 160'
        },
        '05': {
            '_pict': 'terran_vehicle_and_ship_weapons_lvl_2.jpg',
            '_name': 'Vehicle and Ship Weapons Level 2',
            '_desc': 'Further upgrades the damage of Terran Factory and '
                     'Starport units.',
            '01': 'Hotkey: V',
            '02': 'Research From: Armory',
            '03': 'Cost: Minerals 175, Gas 175, Time 190'
        },
        '06': {
            '_pict': 'terran_vehicle_and_ship_weapons_lvl_3.jpg',
            '_name': 'Vehicle and Ship Weapons Level 3',
            '_desc': 'Maximizes the damage of Terran Factory and Starport '
                     'units.',
            '01': 'Hotkey: V',
            '02': 'Research From: Armory',
            '03': 'Cost: Minerals 175, Gas 175, Time 190'
        }
    },
    '01': 'Race: Terran',
    '02': 'Type: Air Unit',
    '03': 'Built From: Starport',
    '04': 'Cost: Minerals 150, Gas 75, Time 42, Supply 2',
    '05': 'Attributes: Armored, Mechanical',
    '06': 'Ground Attack: 12(+1)',
    '07': 'Ground DPS: 12(+1)',
    '08': 'Air Attack: 10(+1)*2',
    '09': 'Air Attack vs. Armored Air: 14(+1)*2',
    '10': 'Air DPS: 10(+1)',
    '11': 'Air DPS vs. Armored Air: 14(+1)',
    '12': 'Ground Attack Range: 6',
    '13': 'Air Attack Range: 9',
    '14': 'Ground Attack Cooldown: 1',
    '15': 'Air Attack Cooldown: 2',
    '16': 'Life: 125',
    '17': 'Armor: 0(+1)',
    '18': 'Hotkey: V',
    '19': 'Sight: 10',
    '20': 'Speed on Ground: 2.25',
    '21': 'Speed on Speed: 2.75',
    '22': 'Cargo Size: 2'
}
_MEDIVAC = {
    '_uniq': 'medivac',
    '_pict': 'medivac.png',
    '_name': 'Medivac',
    '_desc': 'Terran air transport ship. Can also heal biological unit.',
    '_abil': {
        '01': {
            '_pict': 'terran_heal.jpg',
            '_name': 'Heal',
            '_desc': 'The Medivac automatically (or on order) heals a '
                     'close-by friendly biological unit.',
            '01': 'Hotkey: E',
            '02': 'Range: 4',
            '03': 'Duration: 4 seconds'

        },
        '02': {
            '_pict': 'terran_load.jpg',
            '_name': 'Load',
            '_desc': 'The Medivac has a cargo space of 8.',
            '01': 'Hotkey: L'
        },
        '03': {
            '_pict': 'terran_ignite_afterburners.jpg',
            '_name': 'Ignite Afterburners',
            '_desc': 'Speed boost that increases Medivac\'s movement speed '
                     'and acceleration to 4.25.',
            '01': 'Hotkey: B',
            '02': 'Cooldown: 20 seconds',
            '03': 'Duration: 8 seconds'
        },
    },
    '_upgd': {
        '01': {
            '_pict': 'terran_vehicle_and_ship_plating_lvl_1.jpg',
            '_name': 'Vehicle and Ship Plating Level 1',
            '_desc': 'Upgrades the armor of Terran Factory and Starport '
                     'units.',
            '01': 'Hotkey: E',
            '02': 'Research From: Armory',
            '03': 'Cost: Minerals 100, Gas 100, Time 160'
        },
        '02': {
            '_pict': 'terran_vehicle_and_ship_plating_lvl_2.jpg',
            '_name': 'Vehicle and Ship Plating Level 2',
            '_desc': 'Further upgrades the armor of Terran Factory and '
                     'Starport units.',
            '01': 'Hotkey: E',
            '02': 'Research From: Armory',
            '03': 'Cost: Minerals 175, Gas 175, Time 190'
        },
        '03': {
            '_pict': 'terran_vehicle_and_ship_plating_lvl_3.jpg',
            '_name': 'Vehicle and Ship Plating Level 3',
            '_desc': 'Maximizes the armor of Terran Factory and Starport '
                     'units.',
            '01': 'Hotkey: E',
            '02': 'Research From: Armory',
            '03': 'Cost: Minerals 250, Gas 250, Time 220'
        },
        '04': {
            '_pict': 'terran_caduceus_reactor.jpg',
            '_name': 'Caduceus Reactor',
            '_desc': 'Increases the Medivac\'s starting energy by 25.',
            '01': 'Hotkey: A',
            '02': 'Research From: Tech Lab (Attached to Starport)',
            '03': 'Cost: Minerals 100, Gas 100, Time 80'
        }
    },
    '01': 'Race: Terran',
    '02': 'Type: Air Unit',
    '03': 'Built From: Starport',
    '04': 'Cost: Minerals 100, Gas 100, Time 42, Supply 2',
    '05': 'Attributes: Armored, Mechanical',
    '06': 'Life: 150',
    '07': 'Armor: 1(+1)',
    '08': 'Hotkey: D',
    '09': 'Energy: 50(+25)/200',
    '10': 'Sight: 11',
    '11': 'Speed: 2.5'
}
_RAVEN = {
    '_uniq': 'raven',
    '_pict': 'raven.png',
    '_name': 'Raven',
    '_desc': 'Aerial support unit. Can use Auto turrent, Point Defense Drone '
             'and Seeker Missiles abilities.',
    '_abil': {
        '01': {
            '_pict': 'terran_detector.jpg',
            '_name': 'Detector',
            '_desc': 'The Raven is a Detector unit that can see cloaked, '
                     'burrowed and hallucinated units.',
            '01': 'Range: 11'
        },
        '02': {
            '_pict': 'terran_build_auto_turrent.jpg',
            '_name': 'Build Auto-Turret',
            '_desc': 'Automated defensive turret. Times out after 180(+60) '
                     'seconds. Can attack ground and air units.',
            '01': 'Hotkey: T',
            '02': 'Cost: Energy 50',
            '03': 'Range: 3',
            '04': 'Duration: 180(+60) seconds',
            '05': 'Radius: 6(+1)'
        },
        '03': {
            '_pict': 'terran_build_point_defense_drone.jpg',
            '_name': 'Build Point Defense Drone',
            '_desc': 'Uses a laser to shoot down enemy missiles. Cannot '
                     'target special attacks. Times out after 180(+60) '
                     'seconds. Each shot consumes 10 energy.',
            '01': 'Hotkey: D',
            '02': 'Cost: Energy 100',
            '03': 'Range: 3',
            '04': 'Duration: 180(+60) seconds',
            '05': 'Radius: 8(+1)'
        },
        '04': {
            '_pict': 'terran_seeker_missile.jpg',
            '_name': 'Seeker Missile',
            '_desc': 'Missile comes out and stays immobile in front of the '
                     'Raven for 5 seconds while charging up, then rapidly '
                     'moves (it\'s not dodgeable at this point) and explodes '
                     'at the target, causing 100 damage to target plus splash '
                     'damage. Targeted unit lights up red when targeted. If '
                     'the unit moves 13 range out of where the Seeker Missile '
                     'is, the Missile fizzles.',
            '01': 'Hotkey: R',
            '02': 'Cost: Energy 75',
            '03': 'Range: 10'
        }
    },
    '_upgd': {
        '01': {
            '_pict': 'terran_vehicle_and_ship_plating_lvl_1.jpg',
            '_name': 'Vehicle and Ship Plating Level 1',
            '_desc': 'Upgrades the armor of Terran Factory and Starport '
                     'units.',
            '01': 'Hotkey: E',
            '02': 'Research From: Armory',
            '03': 'Cost: Minerals 100, Gas 100, Time 160'
        },
        '02': {
            '_pict': 'terran_vehicle_and_ship_plating_lvl_2.jpg',
            '_name': 'Vehicle and Ship Plating Level 2',
            '_desc': 'Further upgrades the armor of Terran Factory 5&and '
                     'Starport units.',
            '01': 'Hotkey: E',
            '02': 'Research From: Armory',
            '03': 'Cost: Minerals 175, Gas 175, Time 190'
        },
        '03': {
            '_pict': 'terran_vehicle_and_ship_plating_lvl_3.jpg',
            '_name': 'Vehicle and Ship Plating Level 3',
            '_desc': 'Maximizes the armor of Terran Factory and Starport '
                     'units.',
            '01': 'Hotkey: E',
            '02': 'Research From: Armory',
            '03': 'Cost: Minerals 250, Gas 250, Time 220'
        },
        '04': {
            '_pict': 'terran_durable_materials.jpg',
            '_name': 'Durable Materials',
            '_desc': 'Increases the duration of Auto-Turrets and Point '
                     'Defense Drones from 180 to 240 seconds.',
            '01': 'Hotkey: D',
            '02': 'Research From: Engineering Bay',
            '03': 'Cost: Minerals 150, Gas 150, Time 110'
        },
        '05': {
            '_pict': 'terran_corvid_reactor.jpg',
            '_name': 'Corvid Reactor',
            '_desc': 'Increases the Raven\'s starting energy by 25.',
            '01': 'Hotkey: T',
            '02': 'Research From: Tech Lab (Attached to Starport)',
            '03': 'Cost: Minerals 150, Gas 150, Time 110'
        }
    },
    '01': 'Race: Terran',
    '02': 'Type: Air Unit',
    '03': 'Built From: Starport',
    '04': 'Cost: Minerals 100, Gas 200, Time 60, Supply 2',
    '05': 'Attributes: Light, Mechanical, Supply 2',
    '06': 'Life: 140',
    '07': 'Armor: 1(+1)',
    '08': 'Energy: 50(+25)/200',
    '09': 'Sight: 11',
    '10': 'Speed: 2.25'
}
_BANSHEE = {
    '_uniq': 'banshee',
    '_pict': 'banshee.png',
    '_name': 'Banshee',
    '_desc': 'Tactical strike aircraft.',
    '_abil': {
        '01': {
            '_pict': 'terran_cloak.jpg',
            '_name': 'Cloak',
            '_desc': 'The Banshee cloaks itself, turning invisible until it '
                     'runs out of energy.',
            '01': 'Hotkey: C',
            '02': 'Cost: Energy 25, then 0.9/second'
        },
    },
    '_upgd': {
        '01': {
            '_pict': 'terran_vehicle_and_ship_plating_lvl_1.jpg',
            '_name': 'Vehicle and Ship Plating Level 1',
            '_desc': 'Upgrades the armor of Terran Factory and Starport '
                     'units.',
            '01': 'Hotkey: E',
            '02': 'Research From: Armory',
            '03': 'Cost: Minerals 100, Gas 100, Time 160'
        },
        '02': {
            '_pict': 'terran_vehicle_and_ship_plating_lvl_2.jpg',
            '_name': 'Vehicle and Ship Plating Level 2',
            '_desc': 'Further upgrades the armor of Terran Factory and '
                     'Starport units.',
            '01': 'Hotkey: E',
            '02': 'Research From: Armory',
            '03': 'Cost: Minerals 175, Gas 175, Time 190'
        },
        '03': {
            '_pict': 'terran_vehicle_and_ship_plating_lvl_3.jpg',
            '_name': 'Vehicle and Ship Plating Level 3',
            '_desc': 'Maximizes the armor of Terran Factory and Starport '
                     'units.',
            '01': 'Hotkey: E',
            '02': 'Research From: Armory',
            '03': 'Cost: Minerals 250, Gas 250, Time 220'
        },
        '04': {
            '_pict': 'terran_vehicle_and_ship_weapons_lvl_1.jpg',
            '_name': 'Vehicle and Ship Weapons Level 1',
            '_desc': 'Upgrades the damage of Terran Factory and Starport '
                     'units.',
            '01': 'Hotkey: V',
            '02': 'Research From: Armory',
            '03': 'Cost: Minerals 100, Gas 100, Time 160'
        },
        '05': {
            '_pict': 'terran_vehicle_and_ship_weapons_lvl_2.jpg',
            '_name': 'Vehicle and Ship Weapons Level 2',
            '_desc': 'Further upgrades the damage of Terran Factory and '
                     'Starport units.',
            '01': 'Hotkey: V',
            '02': 'Research From: Armory',
            '03': 'Cost: Minerals 175, Gas 175, Time 190'
        },
        '06': {
            '_pict': 'terran_vehicle_and_ship_weapons_lvl_3.jpg',
            '_name': 'Vehicle and Ship Weapons Level 3',
            '_desc': 'Maximizes the damage of Terran Factory and Starport '
                     'units.',
            '01': 'Hotkey: V',
            '02': 'Research From: Armory',
            '03': 'Cost: Minerals 175, Gas 175, Time 190'
        },
        '07': {
            '_pict': 'terran_cloak.jpg',
            '_name': 'Cloaking',
            '_desc': 'Allows Banshees to use Cloak ability.',
            '01': 'Hotkey: C',
            '02': 'Research From: Tech Lab (Attached to Starport)',
            '03': 'Cost: Minerals 100, Gas 100, Time 110'
        }
    },
    '01': 'Race: Terran',
    '02': 'Type: Air Unit',
    '03': 'Built From: Starport',
    '04': 'Cost: Minerals 150, Gas 100, Time 60, Supply 3',
    '05': 'Attributes: Light, Mechanical',
    '06': 'Ground Attack: 12(+1)*2',
    '07': 'Ground DPS: 19.2(+1.6)',
    '08': 'Attack Range: 6',
    '09': 'Attack Cooldown: 1.25',
    '10': 'Life: 140',
    '11': 'Armor: 0(+1)',
    '12': 'Hotkey: E',
    '13': 'Energy: 50/200',
    '14': 'Sight: 10',
    '15': 'Speed: 2.75'
}
_BATTLECRUISER = {
    '_uniq': 'battlecruiser',
    '_pict': 'battlecruiser.png',
    '_name': 'Battlecruiser',
    '_desc': 'Powerful warship. Can be upgraded with the Yamato Cannon '
             'ability.',
    '_abil': {
        '01': {
            '_pict': 'terran_yamato_cannon.jpg',
            '_name': 'Yamato Cannon',
            '_desc': 'The Battlecruiser\'s Yamato Cannon fires an intense '
                     'blast of concentrated energy at the target, dealing '
                     '300 points of damage.',
            '01': 'Hotkey: Y',
            '02': 'Cost: Energy 125',
            '03': 'Range: 10',
            '04': 'Duration: 3 seconds'
        }
    },
    '_upgd': {
        '01': {
            '_pict': 'terran_vehicle_and_ship_plating_lvl_1.jpg',
            '_name': 'Vehicle and Ship Plating Level 1',
            '_desc': 'Upgrades the armor of Terran Factory and Starport '
                     'units.',
            '01': 'Hotkey: E',
            '02': 'Research From: Armory',
            '03': 'Cost: Minerals 100, Gas 100, Time 160'
        },
        '02': {
            '_pict': 'terran_vehicle_and_ship_plating_lvl_2.jpg',
            '_name': 'Vehicle and Ship Plating Level 2',
            '_desc': 'Further upgrades the armor of Terran Factory and '
                     'Starport units.',
            '01': 'Hotkey: E',
            '02': 'Research From: Armory',
            '03': 'Cost: Minerals 175, Gas 175, Time 190'
        },
        '03': {
            '_pict': 'terran_vehicle_and_ship_plating_lvl_3.jpg',
            '_name': 'Vehicle and Ship Plating Level 3',
            '_desc': 'Maximizes the armor of Terran Factory and Starport '
                     'units.',
            '01': 'Hotkey: E',
            '02': 'Research From: Armory',
            '03': 'Cost: Minerals 250, Gas 250, Time 220'
        },
        '04': {
            '_pict': 'terran_vehicle_and_ship_weapons_lvl_1.jpg',
            '_name': 'Vehicle and Ship Weapons Level 1',
            '_desc': 'Upgrades the damage of Terran Factory and Starport '
                     'units.',
            '01': 'Hotkey: V',
            '02': 'Research From: Armory',
            '03': 'Cost: Minerals 100, Gas 100, Time 160'
        },
        '05': {
            '_pict': 'terran_vehicle_and_ship_weapons_lvl_2.jpg',
            '_name': 'Vehicle and Ship Weapons Level 2',
            '_desc': 'Further upgrades the damage of Terran Factory and '
                     'Starport units.',
            '01': 'Hotkey: V',
            '02': 'Research From: Armory',
            '03': 'Cost: Minerals 175, Gas 175, Time 190'
        },
        '06': {
            '_pict': 'terran_vehicle_and_ship_weapons_lvl_3.jpg',
            '_name': 'Vehicle and Ship Weapons Level 3',
            '_desc': 'Maximizes the damage of Terran Factory and Starport '
                     'units.',
            '01': 'Hotkey: V',
            '02': 'Research From: Armory',
            '03': 'Cost: Minerals 175, Gas 175, Time 190'
        },
        '07': {
            '_pict': 'terran_behemoth_reactor.jpg',
            '_name': 'Behemoth Reactor',
            '_desc': 'Increases the Battlecruiser\'s starting energy by 25.',
            '01': 'Hotkey: B',
            '02': 'Research From: Fusion Core',
            '03': 'Cost: Minerals 150, Gas 150, Time 80'
        },
        '08': {
            '_pict': 'terran_yamato_cannon.jpg',
            '_name': 'Weapon Refit',
            '_desc': 'Allows Battlecruisers to use the Yamato Cannon ability.',
            '01': 'Hotkey: R',
            '02': 'Research From: Fusion Core',
            '03': 'Cost: Minerals 150, Gas 150, Time 60'
        }
    },
    '01': 'Race: Terran',
    '02': 'Type: Air Unit',
    '03': 'Built From: Starport',
    '04': 'Cost: Minerals 400, Gas 300, Time 90, Supply 6',
    '05': 'Attributes: Armored, Massive, Mechanical',
    '06': 'Ground Attack: 8(+1)',
    '07': 'Ground DPS: 35.6(+4.4)',
    '08': 'Air Attack: 6(+1)',
    '09': 'Air DPS: 26.7(+4.4)',
    '10': 'Attack Range: 6',
    '11': 'Attack Cooldown: 0.225',
    '12': 'Life: 550',
    '13': 'Armor: 3(+1)',
    '14': 'Hotkey: B',
    '15': 'Energy: 50(+25)/200',
    '16': 'Sight: 12',
    '17': 'Speed: 1.875'
}
_AUTO_TURRENT = {
    '_uniq': 'auto_turrent',
    '_pict': 'auto_turrent.png',
    '_name': 'Auto-Turrent',
    '_desc': 'Automated defensive turrent. Times out after 180 seconds.',
    '_upgd': {
        '01': {
            '_pict': 'terran_hi_sec_auto_tracking.jpg',
            '_name': 'Hi-Sec Auto Tracking',
            '_desc': 'Increases the attack range of Missile Turrets, '
                     'Auto-Turrets, Point Defense Drones, and Planetary '
                     'Fortresses by 1.',
            '01': 'Hotkey: H',
            '02': 'Research From: Engineering Bay',
            '03': 'Cost: Minerals 100, Gas 100, Time 80'
        },
        '02': {
            '_pict': 'terran_durable_materials.jpg',
            '_name': 'Durable Materials',
            '_desc': 'Increases the duration of Auto-Turrets and Point '
                     'Defense Drones from 180 to 240 seconds.',
            '01': 'Hotkey: D',
            '02': 'Research From: Engineering Bay',
            '03': 'Cost: Minerals 150, Gas 150, Time 110'
        },
        '03': {
            '_pict': 'terran_building_armor.jpg',
            '_name': 'Building Armor',
            '_desc': 'Increases the armor of the Point Defense Drone, '
                     'Auto-Turret, Missile Turret, Planetary Fortress, '
                     'and all other Terran structures by 2.',
            '01': 'Hotkey: B',
            '02': 'Research From: Engineering Bay',
            '03': 'Cost: Minerals 150, Gas 150, Time 140'
        }

    },
    '01': 'Race: Terran',
    '02': 'Type: Armored Ground Unit',
    '03': 'Cost: Minerals 0, Gas 0, Time 0, Supply 0',
    '04': 'Attributes: Mechanical, Structure, Armored',
    '05': 'Ground Attack: 8',
    '06': 'Ground DPS: 10',
    '07': 'Air Attack: 8',
    '08': 'Air DPS: 10',
    '09': 'Attack Range: 6(+1)',
    '10': 'Attack Cooldown: 0.8',
    '11': 'Life: 150',
    '12': 'Armor: 1(+2)',
    '13': 'Hotkey: T',
    '14': 'Sight: 7'
}
_POINT_DEFENSE_DRONE = {
    '_uniq': 'point_defense_drone',
    '_pict': 'point_defense_drone.png',
    '_name': 'Point Defense Drone',
    '_desc': 'Uses a laser to shoot down enemy missiles within range 8 (9) '
             'at the cost of 10 energy. Cannot target special attacks. '
             'Times out after 180 (240) seconds.',
    '_abil': {
        '01': {
            '_pict': 'terran_point_defense_laser.jpg',
            '_name': 'Point Defense Laser',
            '_desc': 'Automated defensive laser that intercepts enemy '
                     'projectiles. Effective against Marauders, Vikings, '
                     'Banshees, Battlecruisers, Thors, Missile Turrets, '
                     'Stalkers, Phoenixes, Photon Cannons, Queens, Mutalisks, '
                     'Corruptors, Hydralisks, Spore Crawlers.',
            '01': 'Cost: Energy 10/interception',
            '02': 'Range: 8(+1)',
            '03': 'Cooldown: 0',
            '04': 'Duration: 3 seconds'
        }
    },
    '_upgd': {
        '01': {
            '_pict': 'terran_hi_sec_auto_tracking.jpg',
            '_name': 'Hi-Sec Auto Tracking',
            '_desc': 'Increases the attack range of Missile Turrets, '
                     'Auto-Turrets, Point Defense Drones, and Planetary '
                     'Fortresses by 1.',
            '01': 'Hotkey: H',
            '02': 'Research From: Engineering Bay',
            '03': 'Cost: Minerals 100, Gas 100, Time 80'
        },
        '02': {
            '_pict': 'terran_durable_materials.jpg',
            '_name': 'Durable Materials',
            '_desc': 'Increases the duration of Auto-Turrets and Point '
                     'Defense Drones from 180 to 240 seconds.',
            '01': 'Hotkey: D',
            '02': 'Research From: Engineering Bay',
            '03': 'Cost: Minerals 150, Gas 150, Time 110'
        },
        '03': {
            '_pict': 'terran_building_armor.jpg',
            '_name': 'Building Armor',
            '_desc': 'Increases the armor of the Point Defense Drone, '
                     'Auto-Turret, Missile Turret, Planetary Fortress, '
                     'and all other Terran structures by 2.',
            '01': 'Hotkey: B',
            '02': 'Research From: Engineering Bay',
            '03': 'Cost: Minerals 150, Gas 150, Time 140'
        }
    },
    '01': 'Race: Terran',
    '02': 'Type: Air Unit',
    '03': 'Cost: Minerals 0, Gas 0, Time 0, Supply 0',
    '04': 'Attributes: Light, Mechanical, Structure',
    '05': 'Life: 50',
    '06': 'Armor: 0(+2)',
    '07': 'Hotkey: D',
    '08': 'Energy: 200/200',
    '09': 'Sight: 7',
    '10': 'Speed: 0'
}
_HELLBAT = {
    '_uniq': 'hellbat',
    '_pict': 'hellbat.png',
    '_name': 'Hellbat',
    '_desc': 'A tough melee-range unit with conical splash damage.',
    '_abil': {
        '01': {
            '_pict': 'terran_hellion_mode.jpg',
            '_name': 'Hellion Mode',
            '_desc': 'Transforms the Hellbat into its Hellion form. Requires '
                     'the Transformation Servos upgrade.',
            '01': 'Hotkey: E',
            '02': 'Duration: 4 seconds'
        }
    },
    '_upgd': {
        '01': {
            '_pict': 'terran_vehicle_and_ship_plating_lvl_1.jpg',
            '_name': 'Vehicle and Ship Plating Level 1',
            '_desc': 'Upgrades the armor of Terran Factory and Starport '
                     'units.',
            '01': 'Hotkey: E',
            '02': 'Research From: Armory',
            '03': 'Cost: Minerals 100, Gas 100, Time 160'
        },
        '02': {
            '_pict': 'terran_vehicle_and_ship_plating_lvl_2.jpg',
            '_name': 'Vehicle and Ship Plating Level 2',
            '_desc': 'Further upgrades the armor of Terran Factory and '
                     'Starport units.',
            '01': 'Hotkey: E',
            '02': 'Research From: Armory',
            '03': 'Cost: Minerals 175, Gas 175, Time 190'
        },
        '03': {
            '_pict': 'terran_vehicle_and_ship_plating_lvl_3.jpg',
            '_name': 'Vehicle and Ship Plating Level 3',
            '_desc': 'Maximizes the armor of Terran Factory and Starport '
                     'units.',
            '01': 'Hotkey: E',
            '02': 'Research From: Armory',
            '03': 'Cost: Minerals 250, Gas 250, Time 220'
        },
        '04': {
            '_pict': 'terran_vehicle_and_ship_weapons_lvl_1.jpg',
            '_name': 'Vehicle and Ship Weapons Level 1',
            '_desc': 'Upgrades the damage of Terran Factory and Starport '
                     'units.',
            '01': 'Hotkey: V',
            '02': 'Research From: Armory',
            '03': 'Cost: Minerals 100, Gas 100, Time 160'
        },
        '05': {
            '_pict': 'terran_vehicle_and_ship_weapons_lvl_2.jpg',
            '_name': 'Vehicle and Ship Weapons Level 2',
            '_desc': 'Further upgrades the damage of Terran Factory and '
                     'Starport units.',
            '01': 'Hotkey: V',
            '02': 'Research From: Armory',
            '03': 'Cost: Minerals 175, Gas 175, Time 190'
        },
        '06': {
            '_pict': 'terran_vehicle_and_ship_weapons_lvl_3.jpg',
            '_name': 'Vehicle and Ship Weapons Level 3',
            '_desc': 'Maximizes the damage of Terran Factory and Starport '
                     'units.',
            '01': 'Hotkey: V',
            '02': 'Research From: Armory',
            '03': 'Cost: Minerals 175, Gas 175, Time 190'
        },
        '07': {
            '_pict': 'terran_infernal_pre_igniter.jpg',
            '_name': 'Infernal Pre-Igniter',
            '_desc': 'Improves the Hellion\'s bonus against Light units by +5 '
                     'damage and the Hellbat\'s bonus against Light units by '
                     '+12 damage.',
            '01': 'Hotkey: I',
            '02': 'Research From: Tech Lab (Attached to Factory)',
            '03': 'Cost: Minerals 150, Gas 150, Time 110'
        },
        '08': {
            '_pict': 'terran_transformation_servos.jpg',
            '_name': 'Transformation Servos',
            '_desc': 'Allows Hellions and Hellbats to transform between modes '
                     'freely. Requires an Armory.',
            '01': 'Hotkey: T',
            '02': 'Research From: Tech Lab (Attached to Factory)',
            '03': 'Cost: Minerals 150, Gas 150, Time 110'
        }
    },
    '01': 'Race: Terran',
    '02': 'Type: Ground Unit',
    '03': 'Built From: Factory',
    '04': 'Cost: Minerals 100, Gas 0, Time 30, Supply 2',
    '05': 'Attributes: Biological, Light, Mechanical',
    '06': 'Ground Attack: 18(+2, +3 vs. Light)',
    '07': 'Ground Attack vs. Light with Infernal Pre-Igniter: '
          '30(+2, +3 vs. Light)',
    '08': 'Ground DPS: 9(+1, +1.5 vs. Light)',
    '09': 'Ground DPS vs. Light with Infernal Pre-Igniter: '
          '15(+1, +1.5 vs. Light)',
    '10': 'Attack Range: 2',
    '11': 'Attack Cooldown: 2',
    '12': 'Life: 135',
    '13': 'Armor: 0(+1)',
    '14': 'Hotkey: R',
    '15': 'Sight: 10',
    '16': 'Speed: 2.25',
    '17': 'Cargo Size: 4'
}
_WIDOW_MINE = {
    '_uniq': 'widow_mine',
    '_pict': 'widow_mine.png',
    '_name': 'Widow Mine',
    '_desc': 'A Light & Mechanical Mine which can deal splash damage unit '
             'with an extremely slow rate of fire, but high single target '
             'damage.',
    '_abil': {
        '01': {
            '_pict': 'terran_activate_mine.jpg',
            '_name': 'Activate Mine',
            '_desc': 'Burrows the Widow Mine and readies the weapon. '
                     'Cannot move while activated.',
            '01': 'Hotkey: E',
            '02': 'Duration: 3 seconds'
        },
        '02': {
            '_pict': 'terran_sentinel_missiles.jpg',
            '_name': 'Sentinel Missiles',
            '_desc': 'The Widow Mine automatically launches a missile at the '
                     'closest enemy target within 5 range, dealing 125 damage '
                     '(+35 shield damage) to the target and splash damage to '
                     'surrounding units.'
        }
    },
    '_upgd': {
        '01': {
            '_pict': 'terran_vehicle_and_ship_plating_lvl_1.jpg',
            '_name': 'Vehicle and Ship Plating Level 1',
            '_desc': 'Upgrades the armor of Terran Factory and Starport '
                     'units.',
            '01': 'Hotkey: E',
            '02': 'Research From: Armory',
            '03': 'Cost: Minerals 100, Gas 100, Time 160'
        },
        '02': {
            '_pict': 'terran_vehicle_and_ship_plating_lvl_2.jpg',
            '_name': 'Vehicle and Ship Plating Level 2',
            '_desc': 'Further upgrades the armor of Terran Factory and '
                     'Starport units.',
            '01': 'Hotkey: E',
            '02': 'Research From: Armory',
            '03': 'Cost: Minerals 175, Gas 175, Time 190'
        },
        '03': {
            '_pict': 'terran_vehicle_and_ship_plating_lvl_3.jpg',
            '_name': 'Vehicle and Ship Plating Level 3',
            '_desc': 'Maximizes the armor of Terran Factory and Starport '
                     'units.',
            '01': 'Hotkey: E',
            '02': 'Research From: Armory',
            '03': 'Cost: Minerals 250, Gas 250, Time 220'
        },
        '04': {
            '_pict': 'terran_drilling_claws.jpg',
            '_name': 'Drilling Claws',
            '_desc': 'Decreases burrow time of the Widow Mine from 3 seconds '
                     'to 1 second.',
            '01': 'Hotkey: C',
            '02': 'Research From: Tech Lab (Attached to Factory)',
            '03': 'Cost: Minerals 150, Gas 150, Time 110'
        }
    },
    '01': 'Race: Terran',
    '02': 'Type: Ground Unit',
    '03': 'Built From: Factory',
    '04': 'Cost: Minerals 75, Gas 25, Time 40, Supply 2',
    '05': 'Attributes: Mechanical, Light',
    '06': 'Ground Attack: 125 (Splash)',
    '07': 'Ground Attack vs. Shields: 160 (Splash)',
    '08': 'Air Attack: 125 (Splash)',
    '09': 'Air Attack vs. Shields: 160 (Splash)',
    '10': 'Attack Range: 5',
    '11': 'Life: 90',
    '12': 'Armor: 0(+1)',
    '13': 'Hotkey: D',
    '14': 'Sight: 7',
    '15': 'Speed: 2.8125',
    '16': 'Cargo Size: 2'
}

# Constants: Protoss Units and Structs
# Constants: Zerg Units and Structs


# Main
# if __name__ == '__main__':
#     from pymongo import Connection
#     from db import _DB_URL_TMPL
#     from db import _DB_USR
#     from db import _DB_PWD
#     from db import _DB_HOST
#     from db import _DB_PORT
#     from db import _DB_NAME
#     from db import _COLL_TERRAN
#     from db import _COLL_PROTOSS
#     from db import _COLL_ZERG

#     uri = _DB_URL_TMPL % (_DB_USR, _DB_PWD, _DB_HOST, _DB_PORT, _DB_NAME)
#     connection = Connection(uri)
#     database = connection[_DB_NAME]
#     collection = database[_COLL_TERRAN]

#     # Terran units
#     collection.insert(_SCV)
#     collection.insert(_MULE)
#     collection.insert(_MARINE)
#     collection.insert(_MARAUDER)
#     collection.insert(_REAPER)
#     collection.insert(_GHOST)
#     collection.insert(_HELLION)
#     collection.insert(_SIEGE_TANK)
#     collection.insert(_THOR)
#     collection.insert(_VIKING)
#     collection.insert(_MEDIVAC)
#     collection.insert(_RAVEN)
#     collection.insert(_BANSHEE)
#     collection.insert(_BATTLECRUISER)
#     collection.insert(_AUTO_TURRENT)
#     collection.insert(_POINT_DEFENSE_DRONE)
#     collection.insert(_HELLBAT)
#     collection.insert(_WIDOW_MINE)
