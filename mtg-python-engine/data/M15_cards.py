from MTG import card
from MTG import gameobject
from MTG import cardtype
from MTG import static_abilities
from MTG import mana

class c383180(card.Card):
    "Ajani Steadfast"
    def __init__(self):
        super(c383180, self).__init__(gameobject.Characteristics(**{'mana_cost': '3W', 'text': '+1: Until end of turn, up to one target creature gets +1/+1 and gains first strike, vigilance, and lifelink.\n−2: Put a +1/+1 counter on each creature you control and a loyalty counter on each other planeswalker you control.\n−7: You get an emblem with "If a source would deal damage to you or a planeswalker you control, prevent all but 1 of that damage."', 'subtype': ['Ajani'], 'name': 'Ajani Steadfast', 'color': ['W']}, supertype=[], types=[cardtype.CardType.PLANESWALKER], abilities=[static_abilities.StaticAbilities.Vigilance]))

class c383181(card.Card):
    "Ajani's Pridemate"
    def __init__(self):
        super(c383181, self).__init__(gameobject.Characteristics(**{'mana_cost': '1W', 'text': "Whenever you gain life, you may put a +1/+1 counter on Ajani's Pridemate.", 'subtype': ['Cat', 'Soldier'], 'power': 2, 'color': ['W'], 'name': "Ajani's Pridemate", 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383185(card.Card):
    "Avacyn, Guardian Angel"
    def __init__(self):
        super(c383185, self).__init__(gameobject.Characteristics(**{'mana_cost': '2WWW', 'text': 'Flying, vigilance\n{1}{W}: Prevent all damage that would be dealt to another target creature this turn by sources of the color of your choice.\n{5}{W}{W}: Prevent all damage that would be dealt to target player this turn by sources of the color of your choice.', 'subtype': ['Angel'], 'power': 5, 'color': ['W'], 'name': 'Avacyn, Guardian Angel', 'toughness': 4}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying, static_abilities.StaticAbilities.Vigilance]))

class c383188(card.Card):
    "Battle Mastery"
    def __init__(self):
        super(c383188, self).__init__(gameobject.Characteristics(**{'mana_cost': '2W', 'text': 'Enchant creature\nEnchanted creature has double strike. (It deals both first-strike and regular combat damage.)', 'subtype': ['Aura'], 'name': 'Battle Mastery', 'color': ['W']}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c383194(card.Card):
    "Boonweaver Giant"
    def __init__(self):
        super(c383194, self).__init__(gameobject.Characteristics(**{'mana_cost': '6W', 'text': 'When Boonweaver Giant enters the battlefield, you may search your graveyard, hand, and/or library for an Aura card and put it onto the battlefield attached to Boonweaver Giant. If you search your library this way, shuffle it.', 'subtype': ['Giant', 'Monk'], 'power': 4, 'color': ['W'], 'name': 'Boonweaver Giant', 'toughness': 4}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383214(card.Card):
    "Congregate"
    def __init__(self):
        super(c383214, self).__init__(gameobject.Characteristics(**{'mana_cost': '3W', 'text': 'Target player gains 2 life for each creature on the battlefield.', 'name': 'Congregate', 'color': ['W']}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c383215(card.Card):
    "Constricting Sliver"
    def __init__(self):
        super(c383215, self).__init__(gameobject.Characteristics(**{'mana_cost': '5W', 'text': 'Sliver creatures you control have "When this creature enters the battlefield, you may exile target creature an opponent controls until this creature leaves the battlefield."', 'subtype': ['Sliver'], 'power': 3, 'color': ['W'], 'name': 'Constricting Sliver', 'toughness': 3}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383223(card.Card):
    "Dauntless River Marshal"
    def __init__(self):
        super(c383223, self).__init__(gameobject.Characteristics(**{'mana_cost': '1W', 'text': 'Dauntless River Marshal gets +1/+1 as long as you control an Island.\n{3}{U}: Tap target creature.', 'subtype': ['Human', 'Soldier'], 'power': 2, 'color': ['W', 'U'], 'name': 'Dauntless River Marshal', 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383224(card.Card):
    "Devouring Light"
    def __init__(self):
        super(c383224, self).__init__(gameobject.Characteristics(**{'mana_cost': '1WW', 'text': "Convoke (Your creatures can help cast this spell. Each creature you tap while casting this spell pays for {1} or one mana of that creature's color.)\nExile target attacking or blocking creature.", 'name': 'Devouring Light', 'color': ['W']}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[static_abilities.StaticAbilities.Convoke]))

class c383228(card.Card):
    "Divine Favor"
    def __init__(self):
        super(c383228, self).__init__(gameobject.Characteristics(**{'mana_cost': '1W', 'text': 'Enchant creature\nWhen Divine Favor enters the battlefield, you gain 3 life.\nEnchanted creature gets +1/+3.', 'subtype': ['Aura'], 'name': 'Divine Favor', 'color': ['W']}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c383233(card.Card):
    "Ephemeral Shields"
    def __init__(self):
        super(c383233, self).__init__(gameobject.Characteristics(**{'mana_cost': '1W', 'text': 'Convoke (Your creatures can help cast this spell. Each creature you tap while casting this spell pays for {1} or one mana of that creature\'s color.)\nTarget creature gains indestructible until end of turn. (Damage and effects that say "destroy" don\'t destroy it.)', 'name': 'Ephemeral Shields', 'color': ['W']}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[static_abilities.StaticAbilities.Convoke]))

class c383239(card.Card):
    "First Response"
    def __init__(self):
        super(c383239, self).__init__(gameobject.Characteristics(**{'mana_cost': '3W', 'text': 'At the beginning of each upkeep, if you lost life last turn, create a 1/1 white Soldier creature token.', 'name': 'First Response', 'color': ['W']}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c383253(card.Card):
    "Geist of the Moors"
    def __init__(self):
        super(c383253, self).__init__(gameobject.Characteristics(**{'mana_cost': '1WW', 'text': 'Flying', 'subtype': ['Spirit'], 'power': 3, 'color': ['W'], 'name': 'Geist of the Moors', 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying]))

class c383265(card.Card):
    "Heliod's Pilgrim"
    def __init__(self):
        super(c383265, self).__init__(gameobject.Characteristics(**{'mana_cost': '2W', 'text': "When Heliod's Pilgrim enters the battlefield, you may search your library for an Aura card, reveal it, put it into your hand, then shuffle your library.", 'subtype': ['Human', 'Cleric'], 'power': 1, 'color': ['W'], 'name': "Heliod's Pilgrim", 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383272(card.Card):
    "Hushwing Gryff"
    def __init__(self):
        super(c383272, self).__init__(gameobject.Characteristics(**{'mana_cost': '2W', 'text': "Flash\nFlying\nCreatures entering the battlefield don't cause abilities to trigger.", 'subtype': ['Hippogriff'], 'power': 2, 'color': ['W'], 'name': 'Hushwing Gryff', 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flash, static_abilities.StaticAbilities.Flying]))

class c383292(card.Card):
    "Kinsbaile Skirmisher"
    def __init__(self):
        super(c383292, self).__init__(gameobject.Characteristics(**{'mana_cost': '1W', 'text': 'When Kinsbaile Skirmisher enters the battlefield, target creature gets +1/+1 until end of turn.', 'subtype': ['Kithkin', 'Soldier'], 'power': 2, 'color': ['W'], 'name': 'Kinsbaile Skirmisher', 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383303(card.Card):
    "Marked by Honor"
    def __init__(self):
        super(c383303, self).__init__(gameobject.Characteristics(**{'mana_cost': '3W', 'text': "Enchant creature\nEnchanted creature gets +2/+2 and has vigilance. (Attacking doesn't cause it to tap.)", 'subtype': ['Aura'], 'name': 'Marked by Honor', 'color': ['W']}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c383304(card.Card):
    "Mass Calcify"
    def __init__(self):
        super(c383304, self).__init__(gameobject.Characteristics(**{'mana_cost': '5WW', 'text': 'Destroy all nonwhite creatures.', 'name': 'Mass Calcify', 'color': ['W']}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c383306(card.Card):
    "Meditation Puzzle"
    def __init__(self):
        super(c383306, self).__init__(gameobject.Characteristics(**{'mana_cost': '3WW', 'text': "Convoke (Your creatures can help cast this spell. Each creature you tap while casting this spell pays for {1} or one mana of that creature's color.)\nYou gain 8 life.", 'name': 'Meditation Puzzle', 'color': ['W']}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[static_abilities.StaticAbilities.Convoke]))

class c383309(card.Card):
    "Midnight Guard"
    def __init__(self):
        super(c383309, self).__init__(gameobject.Characteristics(**{'mana_cost': '2W', 'text': 'Whenever another creature enters the battlefield, untap Midnight Guard.', 'subtype': ['Human', 'Soldier'], 'power': 2, 'color': ['W'], 'name': 'Midnight Guard', 'toughness': 3}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383332(card.Card):
    "Oppressive Rays"
    def __init__(self):
        super(c383332, self).__init__(gameobject.Characteristics(**{'mana_cost': 'W', 'text': "Enchant creature\nEnchanted creature can't attack or block unless its controller pays {3}.\nActivated abilities of enchanted creature cost {3} more to activate.", 'subtype': ['Aura'], 'name': 'Oppressive Rays', 'color': ['W']}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c383333(card.Card):
    "Oreskos Swiftclaw"
    def __init__(self):
        super(c383333, self).__init__(gameobject.Characteristics(**{'mana_cost': '1W', 'text': '', 'subtype': ['Cat', 'Warrior'], 'power': 3, 'color': ['W'], 'name': 'Oreskos Swiftclaw', 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383339(card.Card):
    "Paragon of New Dawns"
    def __init__(self):
        super(c383339, self).__init__(gameobject.Characteristics(**{'mana_cost': '3W', 'text': "Other white creatures you control get +1/+1.\n{W}, {T}: Another target white creature you control gains vigilance until end of turn. (Attacking doesn't cause it to tap.)", 'subtype': ['Human', 'Soldier'], 'power': 2, 'color': ['W'], 'name': 'Paragon of New Dawns', 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383345(card.Card):
    "Pillar of Light"
    def __init__(self):
        super(c383345, self).__init__(gameobject.Characteristics(**{'mana_cost': '2W', 'text': 'Exile target creature with toughness 4 or greater.', 'name': 'Pillar of Light', 'color': ['W']}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c383352(card.Card):
    "Preeminent Captain"
    def __init__(self):
        super(c383352, self).__init__(gameobject.Characteristics(**{'mana_cost': '2W', 'text': 'First strike (This creature deals combat damage before creatures without first strike.)\nWhenever Preeminent Captain attacks, you may put a Soldier creature card from your hand onto the battlefield tapped and attacking.', 'subtype': ['Kithkin', 'Soldier'], 'power': 2, 'color': ['W'], 'name': 'Preeminent Captain', 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383356(card.Card):
    "Raise the Alarm"
    def __init__(self):
        super(c383356, self).__init__(gameobject.Characteristics(**{'mana_cost': '1W', 'text': 'Create two 1/1 white Soldier creature tokens.', 'name': 'Raise the Alarm', 'color': ['W']}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c383358(card.Card):
    "Razorfoot Griffin"
    def __init__(self):
        super(c383358, self).__init__(gameobject.Characteristics(**{'mana_cost': '3W', 'text': "Flying (This creature can't be blocked except by creatures with flying or reach.)\nFirst strike (This creature deals combat damage before creatures without first strike.)", 'subtype': ['Griffin'], 'power': 2, 'color': ['W'], 'name': 'Razorfoot Griffin', 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying]))

class c383361(card.Card):
    "Resolute Archangel"
    def __init__(self):
        super(c383361, self).__init__(gameobject.Characteristics(**{'mana_cost': '5WW', 'text': 'Flying\nWhen Resolute Archangel enters the battlefield, if your life total is less than your starting life total, it becomes equal to your starting life total.', 'subtype': ['Angel'], 'power': 4, 'color': ['W'], 'name': 'Resolute Archangel', 'toughness': 4}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying]))

class c383363(card.Card):
    "Return to the Ranks"
    def __init__(self):
        super(c383363, self).__init__(gameobject.Characteristics(**{'mana_cost': 'XWW', 'text': "Convoke (Your creatures can help cast this spell. Each creature you tap while casting this spell pays for {1} or one mana of that creature's color.)\nReturn X target creature cards with converted mana cost 2 or less from your graveyard to the battlefield.", 'name': 'Return to the Ranks', 'color': ['W']}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[static_abilities.StaticAbilities.Convoke]))

class c383370(card.Card):
    "Sanctified Charge"
    def __init__(self):
        super(c383370, self).__init__(gameobject.Characteristics(**{'mana_cost': '4W', 'text': 'Creatures you control get +2/+1 until end of turn. White creatures you control also gain first strike until end of turn. (They deal combat damage before creatures without first strike.)', 'name': 'Sanctified Charge', 'color': ['W']}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c383374(card.Card):
    "Selfless Cathar"
    def __init__(self):
        super(c383374, self).__init__(gameobject.Characteristics(**{'mana_cost': 'W', 'text': '{1}{W}, Sacrifice Selfless Cathar: Creatures you control get +1/+1 until end of turn.', 'subtype': ['Human', 'Cleric'], 'power': 1, 'color': ['W'], 'name': 'Selfless Cathar', 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383375(card.Card):
    "Seraph of the Masses"
    def __init__(self):
        super(c383375, self).__init__(gameobject.Characteristics(**{'mana_cost': '5WW', 'text': "Convoke (Your creatures can help cast this spell. Each creature you tap while casting this spell pays for {1} or one mana of that creature's color.)\nFlying\nSeraph of the Masses's power and toughness are each equal to the number of creatures you control.", 'subtype': ['Angel'], 'power': '*', 'color': ['W'], 'name': 'Seraph of the Masses', 'toughness': '*'}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying, static_abilities.StaticAbilities.Convoke]))

class c383386(card.Card):
    "Solemn Offering"
    def __init__(self):
        super(c383386, self).__init__(gameobject.Characteristics(**{'mana_cost': '2W', 'text': 'Destroy target artifact or enchantment. You gain 4 life.', 'name': 'Solemn Offering', 'color': ['W']}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c383391(card.Card):
    "Soul of Theros"
    def __init__(self):
        super(c383391, self).__init__(gameobject.Characteristics(**{'mana_cost': '4WW', 'text': 'Vigilance\n{4}{W}{W}: Creatures you control get +2/+2 and gain first strike and lifelink until end of turn.\n{4}{W}{W}, Exile Soul of Theros from your graveyard: Creatures you control get +2/+2 and gain first strike and lifelink until end of turn.', 'subtype': ['Avatar'], 'power': 6, 'color': ['W'], 'name': 'Soul of Theros', 'toughness': 6}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Vigilance]))

class c383393(card.Card):
    "Soulmender"
    def __init__(self):
        super(c383393, self).__init__(gameobject.Characteristics(**{'mana_cost': 'W', 'text': '{T}: You gain 1 life.', 'subtype': ['Human', 'Cleric'], 'power': 1, 'color': ['W'], 'name': 'Soulmender', 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383394(card.Card):
    "Spectra Ward"
    def __init__(self):
        super(c383394, self).__init__(gameobject.Characteristics(**{'mana_cost': '3WW', 'text': "Enchant creature\nEnchanted creature gets +2/+2 and has protection from all colors. This effect doesn't remove Auras. (It can't be blocked, targeted, or dealt damage by anything that's white, blue, black, red, or green.)", 'subtype': ['Aura'], 'name': 'Spectra Ward', 'color': ['W']}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c383395(card.Card):
    "Spirit Bonds"
    def __init__(self):
        super(c383395, self).__init__(gameobject.Characteristics(**{'mana_cost': '1W', 'text': 'Whenever a nontoken creature enters the battlefield under your control, you may pay {W}. If you do, create a 1/1 white Spirit creature token with flying.\n{1}{W}, Sacrifice a Spirit: Target non-Spirit creature gains indestructible until end of turn. (Damage and effects that say "destroy" don\'t destroy it.)', 'name': 'Spirit Bonds', 'color': ['W']}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c383407(card.Card):
    "Sungrace Pegasus"
    def __init__(self):
        super(c383407, self).__init__(gameobject.Characteristics(**{'mana_cost': '1W', 'text': "Flying (This creature can't be blocked except by creatures with flying or reach.)\nLifelink (Damage dealt by this creature also causes you to gain that much life.)", 'subtype': ['Pegasus'], 'power': 1, 'color': ['W'], 'name': 'Sungrace Pegasus', 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying, static_abilities.StaticAbilities.Lifelink]))

class c383414(card.Card):
    "Tireless Missionaries"
    def __init__(self):
        super(c383414, self).__init__(gameobject.Characteristics(**{'mana_cost': '4W', 'text': 'When Tireless Missionaries enters the battlefield, you gain 3 life.', 'subtype': ['Human', 'Cleric'], 'power': 2, 'color': ['W'], 'name': 'Tireless Missionaries', 'toughness': 3}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383418(card.Card):
    "Triplicate Spirits"
    def __init__(self):
        super(c383418, self).__init__(gameobject.Characteristics(**{'mana_cost': '4WW', 'text': "Convoke (Your creatures can help cast this spell. Each creature you tap while casting this spell pays for {1} or one mana of that creature's color.)\nCreate three 1/1 white Spirit creature tokens with flying. (They can't be blocked except by creatures with flying or reach.)", 'name': 'Triplicate Spirits', 'color': ['W']}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[static_abilities.StaticAbilities.Convoke]))

class c383430(card.Card):
    "Wall of Essence"
    def __init__(self):
        super(c383430, self).__init__(gameobject.Characteristics(**{'mana_cost': '1W', 'text': "Defender (This creature can't attack.)\nWhenever Wall of Essence is dealt combat damage, you gain that much life.", 'subtype': ['Wall'], 'power': 0, 'color': ['W'], 'name': 'Wall of Essence', 'toughness': 4}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Defender]))

class c383435(card.Card):
    "Warden of the Beyond"
    def __init__(self):
        super(c383435, self).__init__(gameobject.Characteristics(**{'mana_cost': '2W', 'text': "Vigilance (Attacking doesn't cause this creature to tap.)\nWarden of the Beyond gets +2/+2 as long as an opponent owns a card in exile.", 'subtype': ['Human', 'Wizard'], 'power': 2, 'color': ['W'], 'name': 'Warden of the Beyond', 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Vigilance]))

class c383177(card.Card):
    "Aeronaut Tinkerer"
    def __init__(self):
        super(c383177, self).__init__(gameobject.Characteristics(**{'mana_cost': '2U', 'text': "Aeronaut Tinkerer has flying as long as you control an artifact. (It can't be blocked except by creatures with flying or reach.)", 'subtype': ['Human', 'Artificer'], 'power': 2, 'color': ['U'], 'name': 'Aeronaut Tinkerer', 'toughness': 3}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383178(card.Card):
    "Aetherspouts"
    def __init__(self):
        super(c383178, self).__init__(gameobject.Characteristics(**{'mana_cost': '3UU', 'text': 'For each attacking creature, its owner puts it on the top or bottom of his or her library.', 'name': 'Aetherspouts', 'color': ['U']}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c383183(card.Card):
    "Amphin Pathmage"
    def __init__(self):
        super(c383183, self).__init__(gameobject.Characteristics(**{'mana_cost': '3U', 'text': "{2}{U}: Target creature can't be blocked this turn.", 'subtype': ['Salamander', 'Wizard'], 'power': 3, 'color': ['U'], 'name': 'Amphin Pathmage', 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383206(card.Card):
    "Chasm Skulker"
    def __init__(self):
        super(c383206, self).__init__(gameobject.Characteristics(**{'mana_cost': '2U', 'text': "Whenever you draw a card, put a +1/+1 counter on Chasm Skulker.\nWhen Chasm Skulker dies, create X 1/1 blue Squid creature tokens with islandwalk, where X is the number of +1/+1 counters on Chasm Skulker. (They can't be blocked as long as defending player controls an Island.)", 'subtype': ['Squid', 'Horror'], 'power': 1, 'color': ['U'], 'name': 'Chasm Skulker', 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383207(card.Card):
    "Chief Engineer"
    def __init__(self):
        super(c383207, self).__init__(gameobject.Characteristics(**{'mana_cost': '1U', 'text': "Artifact spells you cast have convoke. (Your creatures can help cast those spells. Each creature you tap while casting an artifact spell pays for {1} or one mana of that creature's color.)", 'subtype': ['Vedalken', 'Artificer'], 'power': 1, 'color': ['U'], 'name': 'Chief Engineer', 'toughness': 3}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383210(card.Card):
    "Chronostutter"
    def __init__(self):
        super(c383210, self).__init__(gameobject.Characteristics(**{'mana_cost': '5U', 'text': "Put target creature into its owner's library second from the top.", 'name': 'Chronostutter', 'color': ['U']}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c383216(card.Card):
    "Coral Barrier"
    def __init__(self):
        super(c383216, self).__init__(gameobject.Characteristics(**{'mana_cost': '2U', 'text': "Defender (This creature can't attack.)\nWhen Coral Barrier enters the battlefield, create a 1/1 blue Squid creature token with islandwalk. (It can't be blocked as long as defending player controls an Island.)", 'subtype': ['Wall'], 'power': 1, 'color': ['U'], 'name': 'Coral Barrier', 'toughness': 3}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Defender]))

class c383225(card.Card):
    "Diffusion Sliver"
    def __init__(self):
        super(c383225, self).__init__(gameobject.Characteristics(**{'mana_cost': '1U', 'text': 'Whenever a Sliver creature you control becomes the target of a spell or ability an opponent controls, counter that spell or ability unless its controller pays {2}.', 'subtype': ['Sliver'], 'power': 1, 'color': ['U'], 'name': 'Diffusion Sliver', 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383226(card.Card):
    "Dissipate"
    def __init__(self):
        super(c383226, self).__init__(gameobject.Characteristics(**{'mana_cost': '1UU', 'text': "Counter target spell. If that spell is countered this way, exile it instead of putting it into its owner's graveyard.", 'name': 'Dissipate', 'color': ['U']}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c383227(card.Card):
    "Divination"
    def __init__(self):
        super(c383227, self).__init__(gameobject.Characteristics(**{'mana_cost': '2U', 'text': 'Draw two cards.', 'name': 'Divination', 'color': ['U']}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c383230(card.Card):
    "Encrust"
    def __init__(self):
        super(c383230, self).__init__(gameobject.Characteristics(**{'mana_cost': '1UU', 'text': "Enchant artifact or creature\nEnchanted permanent doesn't untap during its controller's untap step and its activated abilities can't be activated.", 'subtype': ['Aura'], 'name': 'Encrust', 'color': ['U']}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c383232(card.Card):
    "Ensoul Artifact"
    def __init__(self):
        super(c383232, self).__init__(gameobject.Characteristics(**{'mana_cost': '1U', 'text': 'Enchant artifact\nEnchanted artifact is a creature with base power and toughness 5/5 in addition to its other types.', 'subtype': ['Aura'], 'name': 'Ensoul Artifact', 'color': ['U']}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c383248(card.Card):
    "Frost Lynx"
    def __init__(self):
        super(c383248, self).__init__(gameobject.Characteristics(**{'mana_cost': '2U', 'text': "When Frost Lynx enters the battlefield, tap target creature an opponent controls. That creature doesn't untap during its controller's next untap step.", 'subtype': ['Elemental', 'Cat'], 'power': 2, 'color': ['U'], 'name': 'Frost Lynx', 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383249(card.Card):
    "Fugitive Wizard"
    def __init__(self):
        super(c383249, self).__init__(gameobject.Characteristics(**{'mana_cost': 'U', 'text': '', 'subtype': ['Human', 'Wizard'], 'power': 1, 'color': ['U'], 'name': 'Fugitive Wizard', 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383256(card.Card):
    "Glacial Crasher"
    def __init__(self):
        super(c383256, self).__init__(gameobject.Characteristics(**{'mana_cost': '4UU', 'text': "Trample (This creature can deal excess combat damage to defending player or planeswalker while attacking.)\nGlacial Crasher can't attack unless there is a Mountain on the battlefield.", 'subtype': ['Elemental'], 'power': 5, 'color': ['U'], 'name': 'Glacial Crasher', 'toughness': 5}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Trample]))

class c383273(card.Card):
    "Hydrosurge"
    def __init__(self):
        super(c383273, self).__init__(gameobject.Characteristics(**{'mana_cost': 'U', 'text': 'Target creature gets -5/-0 until end of turn.', 'name': 'Hydrosurge', 'color': ['U']}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c383274(card.Card):
    "Illusory Angel"
    def __init__(self):
        super(c383274, self).__init__(gameobject.Characteristics(**{'mana_cost': '2U', 'text': "Flying\nCast Illusory Angel only if you've cast another spell this turn.", 'subtype': ['Angel', 'Illusion'], 'power': 4, 'color': ['U'], 'name': 'Illusory Angel', 'toughness': 4}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying]))

class c383278(card.Card):
    "Into the Void"
    def __init__(self):
        super(c383278, self).__init__(gameobject.Characteristics(**{'mana_cost': '3U', 'text': "Return up to two target creatures to their owners' hands.", 'name': 'Into the Void', 'color': ['U']}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c383280(card.Card):
    "Invisibility"
    def __init__(self):
        super(c383280, self).__init__(gameobject.Characteristics(**{'mana_cost': 'UU', 'text': "Enchant creature\nEnchanted creature can't be blocked except by Walls.", 'subtype': ['Aura'], 'name': 'Invisibility', 'color': ['U']}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c383285(card.Card):
    "Jace, the Living Guildpact"
    def __init__(self):
        super(c383285, self).__init__(gameobject.Characteristics(**{'mana_cost': '2UU', 'text': "+1: Look at the top two cards of your library. Put one of them into your graveyard.\n−3: Return another target nonland permanent to its owner's hand.\n−8: Each player shuffles his or her hand and graveyard into his or her library. You draw seven cards.", 'subtype': ['Jace'], 'name': 'Jace, the Living Guildpact', 'color': ['U']}, supertype=[], types=[cardtype.CardType.PLANESWALKER], abilities=[]))

class c383286(card.Card):
    "Jace's Ingenuity"
    def __init__(self):
        super(c383286, self).__init__(gameobject.Characteristics(**{'mana_cost': '3UU', 'text': 'Draw three cards.', 'name': "Jace's Ingenuity", 'color': ['U']}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c383287(card.Card):
    "Jalira, Master Polymorphist"
    def __init__(self):
        super(c383287, self).__init__(gameobject.Characteristics(**{'mana_cost': '3U', 'text': '{2}{U}, {T}, Sacrifice another creature: Reveal cards from the top of your library until you reveal a nonlegendary creature card. Put that card onto the battlefield and the rest on the bottom of your library in a random order.', 'subtype': ['Human', 'Wizard'], 'power': 2, 'color': ['U'], 'name': 'Jalira, Master Polymorphist', 'toughness': 2}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383288(card.Card):
    "Jorubai Murk Lurker"
    def __init__(self):
        super(c383288, self).__init__(gameobject.Characteristics(**{'mana_cost': '2U', 'text': 'Jorubai Murk Lurker gets +1/+1 as long as you control a Swamp.\n{1}{B}: Target creature gains lifelink until end of turn. (Damage dealt by the creature also causes its controller to gain that much life.)', 'subtype': ['Leech'], 'power': 1, 'color': ['U', 'B'], 'name': 'Jorubai Murk Lurker', 'toughness': 3}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383291(card.Card):
    "Kapsho Kitefins"
    def __init__(self):
        super(c383291, self).__init__(gameobject.Characteristics(**{'mana_cost': '4UU', 'text': 'Flying\nWhenever Kapsho Kitefins or another creature enters the battlefield under your control, tap target creature an opponent controls.', 'subtype': ['Fish'], 'power': 3, 'color': ['U'], 'name': 'Kapsho Kitefins', 'toughness': 3}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying]))

class c383305(card.Card):
    "Master of Predicaments"
    def __init__(self):
        super(c383305, self).__init__(gameobject.Characteristics(**{'mana_cost': '3UU', 'text': "Flying\nWhenever Master of Predicaments deals combat damage to a player, choose a card in your hand. That player guesses whether the card's converted mana cost is greater than 4. If the player guessed wrong, you may cast the card without paying its mana cost.", 'subtype': ['Sphinx'], 'power': 4, 'color': ['U'], 'name': 'Master of Predicaments', 'toughness': 4}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying]))

class c383307(card.Card):
    "Mercurial Pretender"
    def __init__(self):
        super(c383307, self).__init__(gameobject.Characteristics(**{'mana_cost': '4U', 'text': 'You may have Mercurial Pretender enter the battlefield as a copy of any creature you control, except it gains "{2}{U}{U}: Return this creature to its owner\'s hand."', 'subtype': ['Shapeshifter'], 'power': 0, 'color': ['U'], 'name': 'Mercurial Pretender', 'toughness': 0}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383311(card.Card):
    "Military Intelligence"
    def __init__(self):
        super(c383311, self).__init__(gameobject.Characteristics(**{'mana_cost': '1U', 'text': 'Whenever you attack with two or more creatures, draw a card.', 'name': 'Military Intelligence', 'color': ['U']}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c383313(card.Card):
    "Mind Sculpt"
    def __init__(self):
        super(c383313, self).__init__(gameobject.Characteristics(**{'mana_cost': '1U', 'text': 'Target opponent puts the top seven cards of his or her library into his or her graveyard.', 'name': 'Mind Sculpt', 'color': ['U']}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c383324(card.Card):
    "Negate"
    def __init__(self):
        super(c383324, self).__init__(gameobject.Characteristics(**{'mana_cost': '1U', 'text': 'Counter target noncreature spell.', 'name': 'Negate', 'color': ['U']}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c383327(card.Card):
    "Nimbus of the Isles"
    def __init__(self):
        super(c383327, self).__init__(gameobject.Characteristics(**{'mana_cost': '4U', 'text': "Flying (This creature can't be blocked except by creatures with flying or reach.)", 'subtype': ['Elemental'], 'power': 3, 'color': ['U'], 'name': 'Nimbus of the Isles', 'toughness': 3}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying]))

class c383338(card.Card):
    "Paragon of Gathering Mists"
    def __init__(self):
        super(c383338, self).__init__(gameobject.Characteristics(**{'mana_cost': '3U', 'text': 'Other blue creatures you control get +1/+1.\n{U}, {T}: Another target blue creature you control gains flying until end of turn.', 'subtype': ['Human', 'Wizard'], 'power': 2, 'color': ['U'], 'name': 'Paragon of Gathering Mists', 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383341(card.Card):
    "Peel from Reality"
    def __init__(self):
        super(c383341, self).__init__(gameobject.Characteristics(**{'mana_cost': '1U', 'text': "Return target creature you control and target creature you don't control to their owners' hands.", 'name': 'Peel from Reality', 'color': ['U']}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c383351(card.Card):
    "Polymorphist's Jest"
    def __init__(self):
        super(c383351, self).__init__(gameobject.Characteristics(**{'mana_cost': '1UU', 'text': 'Until end of turn, each creature target player controls loses all abilities and becomes a blue Frog with base power and toughness 1/1.', 'name': "Polymorphist's Jest", 'color': ['U']}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c383354(card.Card):
    "Quickling"
    def __init__(self):
        super(c383354, self).__init__(gameobject.Characteristics(**{'mana_cost': '1U', 'text': "Flash (You may cast this spell any time you could cast an instant.)\nFlying\nWhen Quickling enters the battlefield, sacrifice it unless you return another creature you control to its owner's hand.", 'subtype': ['Faerie', 'Rogue'], 'power': 2, 'color': ['U'], 'name': 'Quickling', 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flash, static_abilities.StaticAbilities.Flying]))

class c383360(card.Card):
    "Research Assistant"
    def __init__(self):
        super(c383360, self).__init__(gameobject.Characteristics(**{'mana_cost': '1U', 'text': '{3}{U}, {T}: Draw a card, then discard a card.', 'subtype': ['Human', 'Wizard'], 'power': 1, 'color': ['U'], 'name': 'Research Assistant', 'toughness': 3}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383389(card.Card):
    "Soul of Ravnica"
    def __init__(self):
        super(c383389, self).__init__(gameobject.Characteristics(**{'mana_cost': '4UU', 'text': 'Flying\n{5}{U}{U}: Draw a card for each color among permanents you control.\n{5}{U}{U}, Exile Soul of Ravnica from your graveyard: Draw a card for each color among permanents you control.', 'subtype': ['Avatar'], 'power': 6, 'color': ['U'], 'name': 'Soul of Ravnica', 'toughness': 6}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying]))

class c383403(card.Card):
    "Statute of Denial"
    def __init__(self):
        super(c383403, self).__init__(gameobject.Characteristics(**{'mana_cost': '2UU', 'text': 'Counter target spell. If you control a blue creature, draw a card, then discard a card.', 'name': 'Statute of Denial', 'color': ['U']}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c383405(card.Card):
    "Stormtide Leviathan"
    def __init__(self):
        super(c383405, self).__init__(gameobject.Characteristics(**{'mana_cost': '5UUU', 'text': "Islandwalk (This creature can't be blocked as long as defending player controls an Island.)\nAll lands are Islands in addition to their other types.\nCreatures without flying or islandwalk can't attack.", 'subtype': ['Leviathan'], 'power': 8, 'color': ['U'], 'name': 'Stormtide Leviathan', 'toughness': 8}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Islandwalk]))

class c383419(card.Card):
    "Turn to Frog"
    def __init__(self):
        super(c383419, self).__init__(gameobject.Characteristics(**{'mana_cost': '1U', 'text': 'Until end of turn, target creature loses all abilities and becomes a blue Frog with base power and toughness 1/1.', 'name': 'Turn to Frog', 'color': ['U']}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c383429(card.Card):
    "Void Snare"
    def __init__(self):
        super(c383429, self).__init__(gameobject.Characteristics(**{'mana_cost': 'U', 'text': "Return target nonland permanent to its owner's hand.", 'name': 'Void Snare', 'color': ['U']}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c383432(card.Card):
    "Wall of Frost"
    def __init__(self):
        super(c383432, self).__init__(gameobject.Characteristics(**{'mana_cost': '1UU', 'text': "Defender\nWhenever Wall of Frost blocks a creature, that creature doesn't untap during its controller's next untap step.", 'subtype': ['Wall'], 'power': 0, 'color': ['U'], 'name': 'Wall of Frost', 'toughness': 7}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Defender]))

class c383437(card.Card):
    "Welkin Tern"
    def __init__(self):
        super(c383437, self).__init__(gameobject.Characteristics(**{'mana_cost': '1U', 'text': "Flying (This creature can't be blocked except by creatures with flying or reach.)\nWelkin Tern can block only creatures with flying.", 'subtype': ['Bird'], 'power': 2, 'color': ['U'], 'name': 'Welkin Tern', 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying]))

class c383175(card.Card):
    "Accursed Spirit"
    def __init__(self):
        super(c383175, self).__init__(gameobject.Characteristics(**{'mana_cost': '3B', 'text': "Intimidate (This creature can't be blocked except by artifact creatures and/or creatures that share a color with it.)", 'subtype': ['Spirit'], 'power': 3, 'color': ['B'], 'name': 'Accursed Spirit', 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Intimidate]))

class c383191(card.Card):
    "Black Cat"
    def __init__(self):
        super(c383191, self).__init__(gameobject.Characteristics(**{'mana_cost': '1B', 'text': 'When Black Cat dies, target opponent discards a card at random.', 'subtype': ['Zombie', 'Cat'], 'power': 1, 'color': ['B'], 'name': 'Black Cat', 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383193(card.Card):
    "Blood Host"
    def __init__(self):
        super(c383193, self).__init__(gameobject.Characteristics(**{'mana_cost': '3BB', 'text': '{1}{B}, Sacrifice another creature: Put a +1/+1 counter on Blood Host and you gain 2 life.', 'subtype': ['Vampire'], 'power': 3, 'color': ['B'], 'name': 'Blood Host', 'toughness': 3}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383201(card.Card):
    "Carrion Crow"
    def __init__(self):
        super(c383201, self).__init__(gameobject.Characteristics(**{'mana_cost': '2B', 'text': "Flying (This creature can't be blocked except by creatures with flying or reach.)\nCarrion Crow enters the battlefield tapped.", 'subtype': ['Zombie', 'Bird'], 'power': 2, 'color': ['B'], 'name': 'Carrion Crow', 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying]))

class c383202(card.Card):
    "Caustic Tar"
    def __init__(self):
        super(c383202, self).__init__(gameobject.Characteristics(**{'mana_cost': '4BB', 'text': 'Enchant land\nEnchanted land has "{T}: Target player loses 3 life."', 'subtype': ['Aura'], 'name': 'Caustic Tar', 'color': ['B']}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c383208(card.Card):
    "Child of Night"
    def __init__(self):
        super(c383208, self).__init__(gameobject.Characteristics(**{'mana_cost': '1B', 'text': 'Lifelink (Damage dealt by this creature also causes you to gain that much life.)', 'subtype': ['Vampire'], 'power': 2, 'color': ['B'], 'name': 'Child of Night', 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Lifelink]))

class c383217(card.Card):
    "Covenant of Blood"
    def __init__(self):
        super(c383217, self).__init__(gameobject.Characteristics(**{'mana_cost': '6B', 'text': "Convoke (Your creatures can help cast this spell. Each creature you tap while casting this spell pays for {1} or one mana of that creature's color.)\nCovenant of Blood deals 4 damage to target creature or player and you gain 4 life.", 'name': 'Covenant of Blood', 'color': ['B']}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[static_abilities.StaticAbilities.Convoke]))

class c383218(card.Card):
    "Crippling Blight"
    def __init__(self):
        super(c383218, self).__init__(gameobject.Characteristics(**{'mana_cost': 'B', 'text': "Enchant creature\nEnchanted creature gets -1/-1 and can't block.", 'subtype': ['Aura'], 'name': 'Crippling Blight', 'color': ['B']}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c383221(card.Card):
    "Cruel Sadist"
    def __init__(self):
        super(c383221, self).__init__(gameobject.Characteristics(**{'mana_cost': 'B', 'text': '{B}, {T}, Pay 1 life: Put a +1/+1 counter on Cruel Sadist.\n{2}{B}, {T}, Remove X +1/+1 counters from Cruel Sadist: Cruel Sadist deals X damage to target creature.', 'subtype': ['Human', 'Assassin'], 'power': 1, 'color': ['B'], 'name': 'Cruel Sadist', 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383231(card.Card):
    "Endless Obedience"
    def __init__(self):
        super(c383231, self).__init__(gameobject.Characteristics(**{'mana_cost': '4BB', 'text': "Convoke (Your creatures can help cast this spell. Each creature you tap while casting this spell pays for {1} or one mana of that creature's color.)\nPut target creature card from a graveyard onto the battlefield under your control.", 'name': 'Endless Obedience', 'color': ['B']}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[static_abilities.StaticAbilities.Convoke]))

class c383234(card.Card):
    "Eternal Thirst"
    def __init__(self):
        super(c383234, self).__init__(gameobject.Characteristics(**{'mana_cost': '1B', 'text': 'Enchant creature\nEnchanted creature has lifelink and "Whenever a creature an opponent controls dies, put a +1/+1 counter on this creature." (Damage dealt by a creature with lifelink also causes its controller to gain that much life.)', 'subtype': ['Aura'], 'name': 'Eternal Thirst', 'color': ['B']}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c383236(card.Card):
    "Feast on the Fallen"
    def __init__(self):
        super(c383236, self).__init__(gameobject.Characteristics(**{'mana_cost': '2B', 'text': 'At the beginning of each upkeep, if an opponent lost life last turn, put a +1/+1 counter on target creature you control.', 'name': 'Feast on the Fallen', 'color': ['B']}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c383238(card.Card):
    "Festergloom"
    def __init__(self):
        super(c383238, self).__init__(gameobject.Characteristics(**{'mana_cost': '2B', 'text': 'Nonblack creatures get -1/-1 until end of turn.', 'name': 'Festergloom', 'color': ['B']}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c383240(card.Card):
    "Flesh to Dust"
    def __init__(self):
        super(c383240, self).__init__(gameobject.Characteristics(**{'mana_cost': '3BB', 'text': "Destroy target creature. It can't be regenerated.", 'name': 'Flesh to Dust', 'color': ['B']}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c383260(card.Card):
    "Gravedigger"
    def __init__(self):
        super(c383260, self).__init__(gameobject.Characteristics(**{'mana_cost': '3B', 'text': 'When Gravedigger enters the battlefield, you may return target creature card from your graveyard to your hand.', 'subtype': ['Zombie'], 'power': 2, 'color': ['B'], 'name': 'Gravedigger', 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383275(card.Card):
    "In Garruk's Wake"
    def __init__(self):
        super(c383275, self).__init__(gameobject.Characteristics(**{'mana_cost': '7BB', 'text': "Destroy all creatures you don't control and all planeswalkers you don't control.", 'name': "In Garruk's Wake", 'color': ['B']}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c383276(card.Card):
    "Indulgent Tormentor"
    def __init__(self):
        super(c383276, self).__init__(gameobject.Characteristics(**{'mana_cost': '3BB', 'text': 'Flying\nAt the beginning of your upkeep, draw a card unless target opponent sacrifices a creature or pays 3 life.', 'subtype': ['Demon'], 'power': 5, 'color': ['B'], 'name': 'Indulgent Tormentor', 'toughness': 3}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying]))

class c383297(card.Card):
    "Leeching Sliver"
    def __init__(self):
        super(c383297, self).__init__(gameobject.Characteristics(**{'mana_cost': '1B', 'text': 'Whenever a Sliver you control attacks, defending player loses 1 life.', 'subtype': ['Sliver'], 'power': 1, 'color': ['B'], 'name': 'Leeching Sliver', 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383300(card.Card):
    "Liliana Vess"
    def __init__(self):
        super(c383300, self).__init__(gameobject.Characteristics(**{'mana_cost': '3BB', 'text': '+1: Target player discards a card.\n−2: Search your library for a card, then shuffle your library and put that card on top of it.\n−8: Put all creature cards from all graveyards onto the battlefield under your control.', 'subtype': ['Liliana'], 'name': 'Liliana Vess', 'color': ['B']}, supertype=[], types=[cardtype.CardType.PLANESWALKER], abilities=[]))

class c383312(card.Card):
    "Mind Rot"
    def __init__(self):
        super(c383312, self).__init__(gameobject.Characteristics(**{'mana_cost': '2B', 'text': 'Target player discards two cards.', 'name': 'Mind Rot', 'color': ['B']}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c383320(card.Card):
    "Necrobite"
    def __init__(self):
        super(c383320, self).__init__(gameobject.Characteristics(**{'mana_cost': '2B', 'text': "Target creature gains deathtouch until end of turn. Regenerate it. (The next time that creature would be destroyed this turn, it isn't. Instead tap it, remove all damage from it, and remove it from combat. Any amount of damage a creature with deathtouch deals to a creature is enough to destroy it.)", 'name': 'Necrobite', 'color': ['B']}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c383321(card.Card):
    "Necrogen Scudder"
    def __init__(self):
        super(c383321, self).__init__(gameobject.Characteristics(**{'mana_cost': '2B', 'text': 'Flying\nWhen Necrogen Scudder enters the battlefield, you lose 3 life.', 'subtype': ['Horror'], 'power': 3, 'color': ['B'], 'name': 'Necrogen Scudder', 'toughness': 3}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying]))

class c383322(card.Card):
    "Necromancer's Assistant"
    def __init__(self):
        super(c383322, self).__init__(gameobject.Characteristics(**{'mana_cost': '2B', 'text': "When Necromancer's Assistant enters the battlefield, put the top three cards of your library into your graveyard.", 'subtype': ['Zombie'], 'power': 3, 'color': ['B'], 'name': "Necromancer's Assistant", 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383323(card.Card):
    "Necromancer's Stockpile"
    def __init__(self):
        super(c383323, self).__init__(gameobject.Characteristics(**{'mana_cost': '1B', 'text': '{1}{B}, Discard a creature card: Draw a card. If the discarded card was a Zombie card, create a tapped 2/2 black Zombie creature token.', 'name': "Necromancer's Stockpile", 'color': ['B']}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c383326(card.Card):
    "Nightfire Giant"
    def __init__(self):
        super(c383326, self).__init__(gameobject.Characteristics(**{'mana_cost': '4B', 'text': 'Nightfire Giant gets +1/+1 as long as you control a Mountain.\n{4}{R}: Nightfire Giant deals 2 damage to target creature or player.', 'subtype': ['Zombie', 'Giant'], 'power': 4, 'color': ['B', 'R'], 'name': 'Nightfire Giant', 'toughness': 3}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383330(card.Card):
    "Ob Nixilis, Unshackled"
    def __init__(self):
        super(c383330, self).__init__(gameobject.Characteristics(**{'mana_cost': '4BB', 'text': 'Flying, trample\nWhenever an opponent searches his or her library, that player sacrifices a creature and loses 10 life.\nWhenever another creature dies, put a +1/+1 counter on Ob Nixilis, Unshackled.', 'subtype': ['Demon'], 'power': 4, 'color': ['B'], 'name': 'Ob Nixilis, Unshackled', 'toughness': 4}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying, static_abilities.StaticAbilities.Trample]))

class c383340(card.Card):
    "Paragon of Open Graves"
    def __init__(self):
        super(c383340, self).__init__(gameobject.Characteristics(**{'mana_cost': '3B', 'text': 'Other black creatures you control get +1/+1.\n{2}{B}, {T}: Another target black creature you control gains deathtouch until end of turn. (Any amount of damage it deals to a creature is enough to destroy it.)', 'subtype': ['Skeleton', 'Warrior'], 'power': 2, 'color': ['B'], 'name': 'Paragon of Open Graves', 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383366(card.Card):
    "Rotfeaster Maggot"
    def __init__(self):
        super(c383366, self).__init__(gameobject.Characteristics(**{'mana_cost': '4B', 'text': "When Rotfeaster Maggot enters the battlefield, exile target creature card from a graveyard. You gain life equal to that card's toughness.", 'subtype': ['Insect'], 'power': 3, 'color': ['B'], 'name': 'Rotfeaster Maggot', 'toughness': 5}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383376(card.Card):
    "Shadowcloak Vampire"
    def __init__(self):
        super(c383376, self).__init__(gameobject.Characteristics(**{'mana_cost': '4B', 'text': "Pay 2 life: Shadowcloak Vampire gains flying until end of turn. (It can't be blocked except by creatures with flying or reach.)", 'subtype': ['Vampire'], 'power': 4, 'color': ['B'], 'name': 'Shadowcloak Vampire', 'toughness': 3}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383383(card.Card):
    "Sign in Blood"
    def __init__(self):
        super(c383383, self).__init__(gameobject.Characteristics(**{'mana_cost': 'BB', 'text': 'Target player draws two cards and loses 2 life.', 'name': 'Sign in Blood', 'color': ['B']}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c383387(card.Card):
    "Soul of Innistrad"
    def __init__(self):
        super(c383387, self).__init__(gameobject.Characteristics(**{'mana_cost': '4BB', 'text': 'Deathtouch\n{3}{B}{B}: Return up to three target creature cards from your graveyard to your hand.\n{3}{B}{B}, Exile Soul of Innistrad from your graveyard: Return up to three target creature cards from your graveyard to your hand.', 'subtype': ['Avatar'], 'power': 6, 'color': ['B'], 'name': 'Soul of Innistrad', 'toughness': 6}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Deathtouch]))

class c383396(card.Card):
    "Stab Wound"
    def __init__(self):
        super(c383396, self).__init__(gameobject.Characteristics(**{'mana_cost': '2B', 'text': "Enchant creature\nEnchanted creature gets -2/-2.\nAt the beginning of the upkeep of enchanted creature's controller, that player loses 2 life.", 'subtype': ['Aura'], 'name': 'Stab Wound', 'color': ['B']}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c383402(card.Card):
    "Stain the Mind"
    def __init__(self):
        super(c383402, self).__init__(gameobject.Characteristics(**{'mana_cost': '4B', 'text': "Convoke (Your creatures can help cast this spell. Each creature you tap while casting this spell pays for {1} or one mana of that creature's color.)\nChoose a nonland card name. Search target player's graveyard, hand, and library for any number of cards with that name and exile them. Then that player shuffles his or her library.", 'name': 'Stain the Mind', 'color': ['B']}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[static_abilities.StaticAbilities.Convoke]))

class c383420(card.Card):
    "Typhoid Rats"
    def __init__(self):
        super(c383420, self).__init__(gameobject.Characteristics(**{'mana_cost': 'B', 'text': 'Deathtouch (Any amount of damage this deals to a creature is enough to destroy it.)', 'subtype': ['Rat'], 'power': 1, 'color': ['B'], 'name': 'Typhoid Rats', 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Deathtouch]))

class c383422(card.Card):
    "Ulcerate"
    def __init__(self):
        super(c383422, self).__init__(gameobject.Characteristics(**{'mana_cost': 'B', 'text': 'Target creature gets -3/-3 until end of turn. You lose 3 life.', 'name': 'Ulcerate', 'color': ['B']}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c383424(card.Card):
    "Unmake the Graves"
    def __init__(self):
        super(c383424, self).__init__(gameobject.Characteristics(**{'mana_cost': '4B', 'text': "Convoke (Your creatures can help cast this spell. Each creature you tap while casting this spell pays for {1} or one mana of that creature's color.)\nReturn up to two target creature cards from your graveyard to your hand.", 'name': 'Unmake the Graves', 'color': ['B']}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[static_abilities.StaticAbilities.Convoke]))

class c383433(card.Card):
    "Wall of Limbs"
    def __init__(self):
        super(c383433, self).__init__(gameobject.Characteristics(**{'mana_cost': '2B', 'text': "Defender (This creature can't attack.)\nWhenever you gain life, put a +1/+1 counter on Wall of Limbs.\n{5}{B}{B}, Sacrifice Wall of Limbs: Target player loses X life, where X is Wall of Limbs's power.", 'subtype': ['Zombie', 'Wall'], 'power': 0, 'color': ['B'], 'name': 'Wall of Limbs', 'toughness': 3}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Defender]))

class c383436(card.Card):
    "Waste Not"
    def __init__(self):
        super(c383436, self).__init__(gameobject.Characteristics(**{'mana_cost': '1B', 'text': 'Whenever an opponent discards a creature card, create a 2/2 black Zombie creature token.\nWhenever an opponent discards a land card, add {B}{B} to your mana pool.\nWhenever an opponent discards a noncreature, nonland card, draw a card.', 'name': 'Waste Not', 'color': ['B']}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c383439(card.Card):
    "Witch's Familiar"
    def __init__(self):
        super(c383439, self).__init__(gameobject.Characteristics(**{'mana_cost': '2B', 'text': '', 'subtype': ['Frog'], 'power': 2, 'color': ['B'], 'name': "Witch's Familiar", 'toughness': 3}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383440(card.Card):
    "Xathrid Slyblade"
    def __init__(self):
        super(c383440, self).__init__(gameobject.Characteristics(**{'mana_cost': '2B', 'text': "Hexproof (This creature can't be the target of spells or abilities your opponents control.)\n{3}{B}: Until end of turn, Xathrid Slyblade loses hexproof and gains first strike and deathtouch. (It deals combat damage before creatures without first strike. Any amount of damage it deals to a creature is enough to destroy it.)", 'subtype': ['Human', 'Assassin'], 'power': 2, 'color': ['B'], 'name': 'Xathrid Slyblade', 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Hexproof]))

class c383443(card.Card):
    "Zof Shade"
    def __init__(self):
        super(c383443, self).__init__(gameobject.Characteristics(**{'mana_cost': '3B', 'text': '{2}{B}: Zof Shade gets +2/+2 until end of turn.', 'subtype': ['Shade'], 'power': 2, 'color': ['B'], 'name': 'Zof Shade', 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383176(card.Card):
    "Act on Impulse"
    def __init__(self):
        super(c383176, self).__init__(gameobject.Characteristics(**{'mana_cost': '2R', 'text': 'Exile the top three cards of your library. Until end of turn, you may play cards exiled this way. (If you cast a spell this way, you still pay its costs. You can play a land this way only if you have an available land play remaining.)', 'name': 'Act on Impulse', 'color': ['R']}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c383179(card.Card):
    "Aggressive Mining"
    def __init__(self):
        super(c383179, self).__init__(gameobject.Characteristics(**{'mana_cost': '3R', 'text': "You can't play lands.\nSacrifice a land: Draw two cards. Activate this ability only once each turn.", 'name': 'Aggressive Mining', 'color': ['R']}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c383182(card.Card):
    "Altac Bloodseeker"
    def __init__(self):
        super(c383182, self).__init__(gameobject.Characteristics(**{'mana_cost': '1R', 'text': 'Whenever a creature an opponent controls dies, Altac Bloodseeker gets +2/+0 and gains first strike and haste until end of turn. (It deals combat damage before creatures without first strike, and it can attack and {T} as soon as it comes under your control.)', 'subtype': ['Human', 'Berserker'], 'power': 2, 'color': ['R'], 'name': 'Altac Bloodseeker', 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383190(card.Card):
    "Belligerent Sliver"
    def __init__(self):
        super(c383190, self).__init__(gameobject.Characteristics(**{'mana_cost': '2R', 'text': "Sliver creatures you control have menace. (They can't be blocked except by two or more creatures.)", 'subtype': ['Sliver'], 'power': 2, 'color': ['R'], 'name': 'Belligerent Sliver', 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383192(card.Card):
    "Blastfire Bolt"
    def __init__(self):
        super(c383192, self).__init__(gameobject.Characteristics(**{'mana_cost': '5R', 'text': 'Blastfire Bolt deals 5 damage to target creature. Destroy all Equipment attached to that creature.', 'name': 'Blastfire Bolt', 'color': ['R']}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c383195(card.Card):
    "Borderland Marauder"
    def __init__(self):
        super(c383195, self).__init__(gameobject.Characteristics(**{'mana_cost': '1R', 'text': 'Whenever Borderland Marauder attacks, it gets +2/+0 until end of turn.', 'subtype': ['Human', 'Warrior'], 'power': 1, 'color': ['R'], 'name': 'Borderland Marauder', 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383198(card.Card):
    "Brood Keeper"
    def __init__(self):
        super(c383198, self).__init__(gameobject.Characteristics(**{'mana_cost': '3R', 'text': 'Whenever an Aura becomes attached to Brood Keeper, create a 2/2 red Dragon creature token with flying. It has "{R}: This creature gets +1/+0 until end of turn."', 'subtype': ['Human', 'Shaman'], 'power': 2, 'color': ['R'], 'name': 'Brood Keeper', 'toughness': 3}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383199(card.Card):
    "Burning Anger"
    def __init__(self):
        super(c383199, self).__init__(gameobject.Characteristics(**{'mana_cost': '4R', 'text': 'Enchant creature\nEnchanted creature has "{T}: This creature deals damage equal to its power to target creature or player."', 'subtype': ['Aura'], 'name': 'Burning Anger', 'color': ['R']}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c383204(card.Card):
    "Chandra, Pyromaster"
    def __init__(self):
        super(c383204, self).__init__(gameobject.Characteristics(**{'mana_cost': '2RR', 'text': "+1: Chandra, Pyromaster deals 1 damage to target player and 1 damage to up to one target creature that player controls. That creature can't block this turn.\n0: Exile the top card of your library. You may play it this turn.\n−7: Exile the top ten cards of your library. Choose an instant or sorcery card exiled this way and copy it three times. You may cast the copies without paying their mana costs.", 'subtype': ['Chandra'], 'name': 'Chandra, Pyromaster', 'color': ['R']}, supertype=[], types=[cardtype.CardType.PLANESWALKER], abilities=[]))

class c383211(card.Card):
    "Circle of Flame"
    def __init__(self):
        super(c383211, self).__init__(gameobject.Characteristics(**{'mana_cost': '1R', 'text': 'Whenever a creature without flying attacks you or a planeswalker you control, Circle of Flame deals 1 damage to that creature.', 'name': 'Circle of Flame', 'color': ['R']}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c383212(card.Card):
    "Clear a Path"
    def __init__(self):
        super(c383212, self).__init__(gameobject.Characteristics(**{'mana_cost': 'R', 'text': 'Destroy target creature with defender.', 'name': 'Clear a Path', 'color': ['R']}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c383213(card.Card):
    "Cone of Flame"
    def __init__(self):
        super(c383213, self).__init__(gameobject.Characteristics(**{'mana_cost': '3RR', 'text': 'Cone of Flame deals 1 damage to target creature or player, 2 damage to another target creature or player, and 3 damage to a third target creature or player.', 'name': 'Cone of Flame', 'color': ['R']}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c383219(card.Card):
    "Crowd's Favor"
    def __init__(self):
        super(c383219, self).__init__(gameobject.Characteristics(**{'mana_cost': 'R', 'text': "Convoke (Your creatures can help cast this spell. Each creature you tap while casting this spell pays for {1} or one mana of that creature's color.)\nTarget creature gets +1/+0 and gains first strike until end of turn. (It deals combat damage before creatures without first strike.)", 'name': "Crowd's Favor", 'color': ['R']}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[static_abilities.StaticAbilities.Convoke]))

class c383220(card.Card):
    "Crucible of Fire"
    def __init__(self):
        super(c383220, self).__init__(gameobject.Characteristics(**{'mana_cost': '3R', 'text': 'Dragon creatures you control get +3/+3.', 'name': 'Crucible of Fire', 'color': ['R']}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c383245(card.Card):
    "Forge Devil"
    def __init__(self):
        super(c383245, self).__init__(gameobject.Characteristics(**{'mana_cost': 'R', 'text': 'When Forge Devil enters the battlefield, it deals 1 damage to target creature and 1 damage to you.', 'subtype': ['Devil'], 'power': 1, 'color': ['R'], 'name': 'Forge Devil', 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383246(card.Card):
    "Foundry Street Denizen"
    def __init__(self):
        super(c383246, self).__init__(gameobject.Characteristics(**{'mana_cost': 'R', 'text': 'Whenever another red creature enters the battlefield under your control, Foundry Street Denizen gets +1/+0 until end of turn.', 'subtype': ['Goblin', 'Warrior'], 'power': 1, 'color': ['R'], 'name': 'Foundry Street Denizen', 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383247(card.Card):
    "Frenzied Goblin"
    def __init__(self):
        super(c383247, self).__init__(gameobject.Characteristics(**{'mana_cost': 'R', 'text': "Whenever Frenzied Goblin attacks, you may pay {R}. If you do, target creature can't block this turn.", 'subtype': ['Goblin', 'Berserker'], 'power': 1, 'color': ['R'], 'name': 'Frenzied Goblin', 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383254(card.Card):
    "Generator Servant"
    def __init__(self):
        super(c383254, self).__init__(gameobject.Characteristics(**{'mana_cost': '1R', 'text': '{T}, Sacrifice Generator Servant: Add {C}{C} to your mana pool. If that mana is spent on a creature spell, it gains haste until end of turn. (That creature can attack and {T} as soon as it comes under your control.)', 'subtype': ['Elemental'], 'power': 2, 'color': ['R'], 'name': 'Generator Servant', 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383257(card.Card):
    "Goblin Kaboomist"
    def __init__(self):
        super(c383257, self).__init__(gameobject.Characteristics(**{'mana_cost': '1R', 'text': 'At the beginning of your upkeep, create a colorless artifact token named Land Mine with "{R}, Sacrifice this artifact: This artifact deals 2 damage to target attacking creature without flying." Then flip a coin. If you lose the flip, Goblin Kaboomist deals 2 damage to itself.', 'subtype': ['Goblin', 'Warrior'], 'power': 1, 'color': ['R'], 'name': 'Goblin Kaboomist', 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383258(card.Card):
    "Goblin Rabblemaster"
    def __init__(self):
        super(c383258, self).__init__(gameobject.Characteristics(**{'mana_cost': '2R', 'text': 'Other Goblin creatures you control attack each turn if able.\nAt the beginning of combat on your turn, create a 1/1 red Goblin creature token with haste.\nWhenever Goblin Rabblemaster attacks, it gets +1/+0 until end of turn for each other attacking Goblin.', 'subtype': ['Goblin', 'Warrior'], 'power': 2, 'color': ['R'], 'name': 'Goblin Rabblemaster', 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383259(card.Card):
    "Goblin Roughrider"
    def __init__(self):
        super(c383259, self).__init__(gameobject.Characteristics(**{'mana_cost': '2R', 'text': '', 'subtype': ['Goblin', 'Knight'], 'power': 3, 'color': ['R'], 'name': 'Goblin Roughrider', 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383262(card.Card):
    "Hammerhand"
    def __init__(self):
        super(c383262, self).__init__(gameobject.Characteristics(**{'mana_cost': 'R', 'text': "Enchant creature\nWhen Hammerhand enters the battlefield, target creature can't block this turn.\nEnchanted creature gets +1/+1 and has haste. (It can attack and {T} no matter when it came under your control.)", 'subtype': ['Aura'], 'name': 'Hammerhand', 'color': ['R']}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c383264(card.Card):
    "Heat Ray"
    def __init__(self):
        super(c383264, self).__init__(gameobject.Characteristics(**{'mana_cost': 'XR', 'text': 'Heat Ray deals X damage to target creature.', 'name': 'Heat Ray', 'color': ['R']}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c383266(card.Card):
    "Hoarding Dragon"
    def __init__(self):
        super(c383266, self).__init__(gameobject.Characteristics(**{'mana_cost': '3RR', 'text': "Flying\nWhen Hoarding Dragon enters the battlefield, you may search your library for an artifact card, exile it, then shuffle your library.\nWhen Hoarding Dragon dies, you may put the exiled card into its owner's hand.", 'subtype': ['Dragon'], 'power': 4, 'color': ['R'], 'name': 'Hoarding Dragon', 'toughness': 4}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying]))

class c383277(card.Card):
    "Inferno Fist"
    def __init__(self):
        super(c383277, self).__init__(gameobject.Characteristics(**{'mana_cost': '1R', 'text': 'Enchant creature you control\nEnchanted creature gets +2/+0.\n{R}, Sacrifice Inferno Fist: Inferno Fist deals 2 damage to target creature or player.', 'subtype': ['Aura'], 'name': 'Inferno Fist', 'color': ['R']}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c383293(card.Card):
    "Kird Chieftain"
    def __init__(self):
        super(c383293, self).__init__(gameobject.Characteristics(**{'mana_cost': '3R', 'text': 'Kird Chieftain gets +1/+1 as long as you control a Forest.\n{4}{G}: Target creature gets +2/+2 and gains trample until end of turn. (If it would assign enough damage to its blockers to destroy them, you may have it assign the rest of its damage to defending player or planeswalker.)', 'subtype': ['Ape'], 'power': 3, 'color': ['R', 'G'], 'name': 'Kird Chieftain', 'toughness': 3}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383294(card.Card):
    "Krenko's Enforcer"
    def __init__(self):
        super(c383294, self).__init__(gameobject.Characteristics(**{'mana_cost': '1RR', 'text': "Intimidate (This creature can't be blocked except by artifact creatures and/or creatures that share a color with it.)", 'subtype': ['Goblin', 'Warrior'], 'power': 2, 'color': ['R'], 'name': "Krenko's Enforcer", 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Intimidate]))

class c383295(card.Card):
    "Kurkesh, Onakke Ancient"
    def __init__(self):
        super(c383295, self).__init__(gameobject.Characteristics(**{'mana_cost': '2RR', 'text': "Whenever you activate an ability of an artifact, if it isn't a mana ability, you may pay {R}. If you do, copy that ability. You may choose new targets for the copy.", 'subtype': ['Ogre', 'Spirit'], 'power': 4, 'color': ['R'], 'name': 'Kurkesh, Onakke Ancient', 'toughness': 3}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383296(card.Card):
    "Lava Axe"
    def __init__(self):
        super(c383296, self).__init__(gameobject.Characteristics(**{'mana_cost': '4R', 'text': 'Lava Axe deals 5 damage to target player.', 'name': 'Lava Axe', 'color': ['R']}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c383299(card.Card):
    "Lightning Strike"
    def __init__(self):
        super(c383299, self).__init__(gameobject.Characteristics(**{'mana_cost': '1R', 'text': 'Lightning Strike deals 3 damage to target creature or player.', 'name': 'Lightning Strike', 'color': ['R']}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c383310(card.Card):
    "Might Makes Right"
    def __init__(self):
        super(c383310, self).__init__(gameobject.Characteristics(**{'mana_cost': '5R', 'text': 'At the beginning of combat on your turn, if you control each creature on the battlefield with the greatest power, gain control of target creature an opponent controls until end of turn. Untap that creature. It gains haste until end of turn. (It can attack and {T} this turn.)', 'name': 'Might Makes Right', 'color': ['R']}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c383314(card.Card):
    "Miner's Bane"
    def __init__(self):
        super(c383314, self).__init__(gameobject.Characteristics(**{'mana_cost': '4RR', 'text': "{2}{R}: Miner's Bane gets +1/+0 and gains trample until end of turn. (If it would assign enough damage to its blockers to destroy them, you may have it assign the rest of its damage to defending player or planeswalker.)", 'subtype': ['Elemental'], 'power': 6, 'color': ['R'], 'name': "Miner's Bane", 'toughness': 3}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383337(card.Card):
    "Paragon of Fierce Defiance"
    def __init__(self):
        super(c383337, self).__init__(gameobject.Characteristics(**{'mana_cost': '3R', 'text': 'Other red creatures you control get +1/+1.\n{R}, {T}: Another target red creature you control gains haste until end of turn. (It can attack and {T} this turn.)', 'subtype': ['Human', 'Warrior'], 'power': 2, 'color': ['R'], 'name': 'Paragon of Fierce Defiance', 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383367(card.Card):
    "Rummaging Goblin"
    def __init__(self):
        super(c383367, self).__init__(gameobject.Characteristics(**{'mana_cost': '2R', 'text': '{T}, Discard a card: Draw a card.', 'subtype': ['Goblin', 'Rogue'], 'power': 1, 'color': ['R'], 'name': 'Rummaging Goblin', 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383372(card.Card):
    "Scrapyard Mongrel"
    def __init__(self):
        super(c383372, self).__init__(gameobject.Characteristics(**{'mana_cost': '3R', 'text': 'As long as you control an artifact, Scrapyard Mongrel gets +2/+0 and has trample. (If it would assign enough damage to its blockers to destroy them, you may have it assign the rest of its damage to defending player or planeswalker.)', 'subtype': ['Hound'], 'power': 3, 'color': ['R'], 'name': 'Scrapyard Mongrel', 'toughness': 3}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383380(card.Card):
    "Shrapnel Blast"
    def __init__(self):
        super(c383380, self).__init__(gameobject.Characteristics(**{'mana_cost': '1R', 'text': 'As an additional cost to cast Shrapnel Blast, sacrifice an artifact.\nShrapnel Blast deals 5 damage to target creature or player.', 'name': 'Shrapnel Blast', 'color': ['R']}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c383381(card.Card):
    "Siege Dragon"
    def __init__(self):
        super(c383381, self).__init__(gameobject.Characteristics(**{'mana_cost': '5RR', 'text': 'Flying\nWhen Siege Dragon enters the battlefield, destroy all Walls your opponents control.\nWhenever Siege Dragon attacks, if defending player controls no Walls, it deals 2 damage to each creature without flying that player controls.', 'subtype': ['Dragon'], 'power': 5, 'color': ['R'], 'name': 'Siege Dragon', 'toughness': 5}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying]))

class c383390(card.Card):
    "Soul of Shandalar"
    def __init__(self):
        super(c383390, self).__init__(gameobject.Characteristics(**{'mana_cost': '4RR', 'text': 'First strike\n{3}{R}{R}: Soul of Shandalar deals 3 damage to target player and 3 damage to up to one target creature that player controls.\n{3}{R}{R}, Exile Soul of Shandalar from your graveyard: Soul of Shandalar deals 3 damage to target player and 3 damage to up to one target creature that player controls.', 'subtype': ['Avatar'], 'power': 6, 'color': ['R'], 'name': 'Soul of Shandalar', 'toughness': 6}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383404(card.Card):
    "Stoke the Flames"
    def __init__(self):
        super(c383404, self).__init__(gameobject.Characteristics(**{'mana_cost': '2RR', 'text': "Convoke (Your creatures can help cast this spell. Each creature you tap while casting this spell pays for {1} or one mana of that creature's color.)\nStoke the Flames deals 4 damage to target creature or player.", 'name': 'Stoke the Flames', 'color': ['R']}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[static_abilities.StaticAbilities.Convoke]))

class c383413(card.Card):
    "Thundering Giant"
    def __init__(self):
        super(c383413, self).__init__(gameobject.Characteristics(**{'mana_cost': '3RR', 'text': 'Haste (This creature can attack and {T} as soon as it comes under your control.)', 'subtype': ['Giant'], 'power': 4, 'color': ['R'], 'name': 'Thundering Giant', 'toughness': 3}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Haste]))

class c383416(card.Card):
    "Torch Fiend"
    def __init__(self):
        super(c383416, self).__init__(gameobject.Characteristics(**{'mana_cost': '1R', 'text': '{R}, Sacrifice Torch Fiend: Destroy target artifact.', 'subtype': ['Devil'], 'power': 2, 'color': ['R'], 'name': 'Torch Fiend', 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383431(card.Card):
    "Wall of Fire"
    def __init__(self):
        super(c383431, self).__init__(gameobject.Characteristics(**{'mana_cost': '1RR', 'text': "Defender (This creature can't attack.)\n{R}: Wall of Fire gets +1/+0 until end of turn.", 'subtype': ['Wall'], 'power': 0, 'color': ['R'], 'name': 'Wall of Fire', 'toughness': 5}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Defender]))

class c383184(card.Card):
    "Ancient Silverback"
    def __init__(self):
        super(c383184, self).__init__(gameobject.Characteristics(**{'mana_cost': '4GG', 'text': "{G}: Regenerate Ancient Silverback. (The next time this creature would be destroyed this turn, it isn't. Instead tap it, remove all damage from it, and remove it from combat.)", 'subtype': ['Ape'], 'power': 6, 'color': ['G'], 'name': 'Ancient Silverback', 'toughness': 5}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383187(card.Card):
    "Back to Nature"
    def __init__(self):
        super(c383187, self).__init__(gameobject.Characteristics(**{'mana_cost': '1G', 'text': 'Destroy all enchantments.', 'name': 'Back to Nature', 'color': ['G']}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c383200(card.Card):
    "Carnivorous Moss-Beast"
    def __init__(self):
        super(c383200, self).__init__(gameobject.Characteristics(**{'mana_cost': '4GG', 'text': '{5}{G}{G}: Put a +1/+1 counter on Carnivorous Moss-Beast.', 'subtype': ['Plant', 'Elemental', 'Beast'], 'power': 4, 'color': ['G'], 'name': 'Carnivorous Moss-Beast', 'toughness': 5}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383205(card.Card):
    "Charging Rhino"
    def __init__(self):
        super(c383205, self).__init__(gameobject.Characteristics(**{'mana_cost': '3GG', 'text': "Charging Rhino can't be blocked by more than one creature.", 'subtype': ['Rhino'], 'power': 4, 'color': ['G'], 'name': 'Charging Rhino', 'toughness': 4}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383209(card.Card):
    "Chord of Calling"
    def __init__(self):
        super(c383209, self).__init__(gameobject.Characteristics(**{'mana_cost': 'XGGG', 'text': "Convoke (Your creatures can help cast this spell. Each creature you tap while casting this spell pays for {1} or one mana of that creature's color.)\nSearch your library for a creature card with converted mana cost X or less and put it onto the battlefield. Then shuffle your library.", 'name': 'Chord of Calling', 'color': ['G']}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[static_abilities.StaticAbilities.Convoke]))

class c383229(card.Card):
    "Elvish Mystic"
    def __init__(self):
        super(c383229, self).__init__(gameobject.Characteristics(**{'mana_cost': 'G', 'text': '{T}: Add {G} to your mana pool.', 'subtype': ['Elf', 'Druid'], 'power': 1, 'color': ['G'], 'name': 'Elvish Mystic', 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383237(card.Card):
    "Feral Incarnation"
    def __init__(self):
        super(c383237, self).__init__(gameobject.Characteristics(**{'mana_cost': '8G', 'text': "Convoke (Your creatures can help cast this spell. Each creature you tap while casting this spell pays for {1} or one mana of that creature's color.)\nCreate three 3/3 green Beast creature tokens.", 'name': 'Feral Incarnation', 'color': ['G']}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[static_abilities.StaticAbilities.Convoke]))

class c383252(card.Card):
    "Gather Courage"
    def __init__(self):
        super(c383252, self).__init__(gameobject.Characteristics(**{'mana_cost': 'G', 'text': "Convoke (Your creatures can help cast this spell. Each creature you tap while casting this spell pays for {1} or one mana of that creature's color.)\nTarget creature gets +2/+2 until end of turn.", 'name': 'Gather Courage', 'color': ['G']}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[static_abilities.StaticAbilities.Convoke]))

class c383255(card.Card):
    "Genesis Hydra"
    def __init__(self):
        super(c383255, self).__init__(gameobject.Characteristics(**{'mana_cost': 'XGG', 'text': 'When you cast Genesis Hydra, reveal the top X cards of your library. You may put a nonland permanent card with converted mana cost X or less from among them onto the battlefield. Then shuffle the rest into your library.\nGenesis Hydra enters the battlefield with X +1/+1 counters on it.', 'subtype': ['Plant', 'Hydra'], 'power': 0, 'color': ['G'], 'name': 'Genesis Hydra', 'toughness': 0}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383267(card.Card):
    "Hornet Nest"
    def __init__(self):
        super(c383267, self).__init__(gameobject.Characteristics(**{'mana_cost': '2G', 'text': "Defender (This creature can't attack.)\nWhenever Hornet Nest is dealt damage, create that many 1/1 green Insect creature tokens with flying and deathtouch. (Any amount of damage a creature with deathtouch deals to a creature is enough to destroy it.)", 'subtype': ['Insect'], 'power': 0, 'color': ['G'], 'name': 'Hornet Nest', 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Defender]))

class c383268(card.Card):
    "Hornet Queen"
    def __init__(self):
        super(c383268, self).__init__(gameobject.Characteristics(**{'mana_cost': '4GGG', 'text': 'Flying\nDeathtouch (Any amount of damage this deals to a creature is enough to destroy it.)\nWhen Hornet Queen enters the battlefield, create four 1/1 green Insect creature tokens with flying and deathtouch.', 'subtype': ['Insect'], 'power': 2, 'color': ['G'], 'name': 'Hornet Queen', 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Deathtouch, static_abilities.StaticAbilities.Flying]))

class c383270(card.Card):
    "Hunt the Weak"
    def __init__(self):
        super(c383270, self).__init__(gameobject.Characteristics(**{'mana_cost': '3G', 'text': "Put a +1/+1 counter on target creature you control. Then that creature fights target creature you don't control. (Each deals damage equal to its power to the other.)", 'name': 'Hunt the Weak', 'color': ['G']}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c383271(card.Card):
    "Hunter's Ambush"
    def __init__(self):
        super(c383271, self).__init__(gameobject.Characteristics(**{'mana_cost': '2G', 'text': 'Prevent all combat damage that would be dealt by nongreen creatures this turn.', 'name': "Hunter's Ambush", 'color': ['G']}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c383279(card.Card):
    "Invasive Species"
    def __init__(self):
        super(c383279, self).__init__(gameobject.Characteristics(**{'mana_cost': '2G', 'text': "When Invasive Species enters the battlefield, return another permanent you control to its owner's hand.", 'subtype': ['Insect'], 'power': 3, 'color': ['G'], 'name': 'Invasive Species', 'toughness': 3}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383290(card.Card):
    "Kalonian Twingrove"
    def __init__(self):
        super(c383290, self).__init__(gameobject.Characteristics(**{'mana_cost': '5G', 'text': 'Kalonian Twingrove\'s power and toughness are each equal to the number of Forests you control.\nWhen Kalonian Twingrove enters the battlefield, create a green Treefolk Warrior creature token with "This creature\'s power and toughness are each equal to the number of Forests you control."', 'subtype': ['Treefolk', 'Warrior'], 'power': '*', 'color': ['G'], 'name': 'Kalonian Twingrove', 'toughness': '*'}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383298(card.Card):
    "Life's Legacy"
    def __init__(self):
        super(c383298, self).__init__(gameobject.Characteristics(**{'mana_cost': '1G', 'text': "As an additional cost to cast Life's Legacy, sacrifice a creature.\nDraw cards equal to the sacrificed creature's power.", 'name': "Life's Legacy", 'color': ['G']}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c383301(card.Card):
    "Living Totem"
    def __init__(self):
        super(c383301, self).__init__(gameobject.Characteristics(**{'mana_cost': '3G', 'text': "Convoke (Your creatures can help cast this spell. Each creature you tap while casting this spell pays for {1} or one mana of that creature's color.)\nWhen Living Totem enters the battlefield, you may put a +1/+1 counter on another target creature.", 'subtype': ['Plant', 'Elemental'], 'power': 2, 'color': ['G'], 'name': 'Living Totem', 'toughness': 3}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Convoke]))

class c383319(card.Card):
    "Naturalize"
    def __init__(self):
        super(c383319, self).__init__(gameobject.Characteristics(**{'mana_cost': '1G', 'text': 'Destroy target artifact or enchantment.', 'name': 'Naturalize', 'color': ['G']}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c383325(card.Card):
    "Netcaster Spider"
    def __init__(self):
        super(c383325, self).__init__(gameobject.Characteristics(**{'mana_cost': '2G', 'text': 'Reach (This creature can block creatures with flying.)\nWhenever Netcaster Spider blocks a creature with flying, Netcaster Spider gets +2/+0 until end of turn.', 'subtype': ['Spider'], 'power': 2, 'color': ['G'], 'name': 'Netcaster Spider', 'toughness': 3}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Reach]))

class c383328(card.Card):
    "Nissa, Worldwaker"
    def __init__(self):
        super(c383328, self).__init__(gameobject.Characteristics(**{'mana_cost': '3GG', 'text': "+1: Target land you control becomes a 4/4 Elemental creature with trample. It's still a land.\n+1: Untap up to four target Forests.\n−7: Search your library for any number of basic land cards, put them onto the battlefield, then shuffle your library. Those lands become 4/4 Elemental creatures with trample. They're still lands.", 'subtype': ['Nissa'], 'name': 'Nissa, Worldwaker', 'color': ['G']}, supertype=[], types=[cardtype.CardType.PLANESWALKER], abilities=[]))

class c383329(card.Card):
    "Nissa's Expedition"
    def __init__(self):
        super(c383329, self).__init__(gameobject.Characteristics(**{'mana_cost': '4G', 'text': "Convoke (Your creatures can help cast this spell. Each creature you tap while casting this spell pays for {1} or one mana of that creature's color.)\nSearch your library for up to two basic land cards, put them onto the battlefield tapped, then shuffle your library.", 'name': "Nissa's Expedition", 'color': ['G']}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[static_abilities.StaticAbilities.Convoke]))

class c383335(card.Card):
    "Overwhelm"
    def __init__(self):
        super(c383335, self).__init__(gameobject.Characteristics(**{'mana_cost': '5GG', 'text': "Convoke (Your creatures can help cast this spell. Each creature you tap while casting this spell pays for {1} or one mana of that creature's color.)\nCreatures you control get +3/+3 until end of turn.", 'name': 'Overwhelm', 'color': ['G']}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[static_abilities.StaticAbilities.Convoke]))

class c383336(card.Card):
    "Paragon of Eternal Wilds"
    def __init__(self):
        super(c383336, self).__init__(gameobject.Characteristics(**{'mana_cost': '3G', 'text': 'Other green creatures you control get +1/+1.\n{G}, {T}: Another target green creature you control gains trample until end of turn. (If it would assign enough damage to its blockers to destroy them, you may have it assign the rest of its damage to defending player or planeswalker.)', 'subtype': ['Human', 'Druid'], 'power': 2, 'color': ['G'], 'name': 'Paragon of Eternal Wilds', 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383344(card.Card):
    "Phytotitan"
    def __init__(self):
        super(c383344, self).__init__(gameobject.Characteristics(**{'mana_cost': '4GG', 'text': "When Phytotitan dies, return it to the battlefield tapped under its owner's control at the beginning of his or her next upkeep.", 'subtype': ['Plant', 'Elemental'], 'power': 7, 'color': ['G'], 'name': 'Phytotitan', 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383350(card.Card):
    "Plummet"
    def __init__(self):
        super(c383350, self).__init__(gameobject.Characteristics(**{'mana_cost': '1G', 'text': 'Destroy target creature with flying.', 'name': 'Plummet', 'color': ['G']}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c383357(card.Card):
    "Ranger's Guile"
    def __init__(self):
        super(c383357, self).__init__(gameobject.Characteristics(**{'mana_cost': 'G', 'text': "Target creature you control gets +1/+1 and gains hexproof until end of turn. (It can't be the target of spells or abilities your opponents control.)", 'name': "Ranger's Guile", 'color': ['G']}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c383359(card.Card):
    "Reclamation Sage"
    def __init__(self):
        super(c383359, self).__init__(gameobject.Characteristics(**{'mana_cost': '2G', 'text': 'When Reclamation Sage enters the battlefield, you may destroy target artifact or enchantment.', 'subtype': ['Elf', 'Shaman'], 'power': 2, 'color': ['G'], 'name': 'Reclamation Sage', 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383362(card.Card):
    "Restock"
    def __init__(self):
        super(c383362, self).__init__(gameobject.Characteristics(**{'mana_cost': '3GG', 'text': 'Return two target cards from your graveyard to your hand. Exile Restock.', 'name': 'Restock', 'color': ['G']}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c383364(card.Card):
    "Roaring Primadox"
    def __init__(self):
        super(c383364, self).__init__(gameobject.Characteristics(**{'mana_cost': '3G', 'text': "At the beginning of your upkeep, return a creature you control to its owner's hand.", 'subtype': ['Beast'], 'power': 4, 'color': ['G'], 'name': 'Roaring Primadox', 'toughness': 4}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383368(card.Card):
    "Runeclaw Bear"
    def __init__(self):
        super(c383368, self).__init__(gameobject.Characteristics(**{'mana_cost': '1G', 'text': '', 'subtype': ['Bear'], 'power': 2, 'color': ['G'], 'name': 'Runeclaw Bear', 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383371(card.Card):
    "Satyr Wayfinder"
    def __init__(self):
        super(c383371, self).__init__(gameobject.Characteristics(**{'mana_cost': '1G', 'text': 'When Satyr Wayfinder enters the battlefield, reveal the top four cards of your library. You may put a land card from among them into your hand. Put the rest into your graveyard.', 'subtype': ['Satyr'], 'power': 1, 'color': ['G'], 'name': 'Satyr Wayfinder', 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383377(card.Card):
    "Shaman of Spring"
    def __init__(self):
        super(c383377, self).__init__(gameobject.Characteristics(**{'mana_cost': '3G', 'text': 'When Shaman of Spring enters the battlefield, draw a card.', 'subtype': ['Elf', 'Shaman'], 'power': 2, 'color': ['G'], 'name': 'Shaman of Spring', 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383382(card.Card):
    "Siege Wurm"
    def __init__(self):
        super(c383382, self).__init__(gameobject.Characteristics(**{'mana_cost': '5GG', 'text': "Convoke (Your creatures can help cast this spell. Each creature you tap while casting this spell pays for {1} or one mana of that creature's color.)\nTrample (This creature can deal excess combat damage to defending player or planeswalker while attacking.)", 'subtype': ['Wurm'], 'power': 5, 'color': ['G'], 'name': 'Siege Wurm', 'toughness': 5}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Trample, static_abilities.StaticAbilities.Convoke]))

class c383392(card.Card):
    "Soul of Zendikar"
    def __init__(self):
        super(c383392, self).__init__(gameobject.Characteristics(**{'mana_cost': '4GG', 'text': 'Reach\n{3}{G}{G}: Create a 3/3 green Beast creature token.\n{3}{G}{G}, Exile Soul of Zendikar from your graveyard: Create a 3/3 green Beast creature token.', 'subtype': ['Avatar'], 'power': 6, 'color': ['G'], 'name': 'Soul of Zendikar', 'toughness': 6}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Reach]))

class c383406(card.Card):
    "Sunblade Elf"
    def __init__(self):
        super(c383406, self).__init__(gameobject.Characteristics(**{'mana_cost': 'G', 'text': 'Sunblade Elf gets +1/+1 as long as you control a Plains.\n{4}{W}: Creatures you control get +1/+1 until end of turn.', 'subtype': ['Elf', 'Warrior'], 'power': 1, 'color': ['G', 'W'], 'name': 'Sunblade Elf', 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383415(card.Card):
    "Titanic Growth"
    def __init__(self):
        super(c383415, self).__init__(gameobject.Characteristics(**{'mana_cost': '1G', 'text': 'Target creature gets +4/+4 until end of turn.', 'name': 'Titanic Growth', 'color': ['G']}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c383423(card.Card):
    "Undergrowth Scavenger"
    def __init__(self):
        super(c383423, self).__init__(gameobject.Characteristics(**{'mana_cost': '3G', 'text': 'Undergrowth Scavenger enters the battlefield with a number of +1/+1 counters on it equal to the number of creature cards in all graveyards.', 'subtype': ['Fungus', 'Horror'], 'power': 0, 'color': ['G'], 'name': 'Undergrowth Scavenger', 'toughness': 0}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383426(card.Card):
    "Venom Sliver"
    def __init__(self):
        super(c383426, self).__init__(gameobject.Characteristics(**{'mana_cost': '1G', 'text': 'Sliver creatures you control have deathtouch. (Any amount of damage a creature with deathtouch deals to a creature is enough to destroy it.)', 'subtype': ['Sliver'], 'power': 1, 'color': ['G'], 'name': 'Venom Sliver', 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383427(card.Card):
    "Verdant Haven"
    def __init__(self):
        super(c383427, self).__init__(gameobject.Characteristics(**{'mana_cost': '2G', 'text': 'Enchant land\nWhen Verdant Haven enters the battlefield, you gain 2 life.\nWhenever enchanted land is tapped for mana, its controller adds one mana of any color to his or her mana pool (in addition to the mana the land produces).', 'subtype': ['Aura'], 'name': 'Verdant Haven', 'color': ['G']}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c383428(card.Card):
    "Vineweft"
    def __init__(self):
        super(c383428, self).__init__(gameobject.Characteristics(**{'mana_cost': 'G', 'text': 'Enchant creature\nEnchanted creature gets +1/+1.\n{4}{G}: Return Vineweft from your graveyard to your hand.', 'subtype': ['Aura'], 'name': 'Vineweft', 'color': ['G']}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c383434(card.Card):
    "Wall of Mulch"
    def __init__(self):
        super(c383434, self).__init__(gameobject.Characteristics(**{'mana_cost': '1G', 'text': "Defender (This creature can't attack.)\n{G}, Sacrifice a Wall: Draw a card.", 'subtype': ['Wall'], 'power': 0, 'color': ['G'], 'name': 'Wall of Mulch', 'toughness': 4}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Defender]))

class c383442(card.Card):
    "Yisan, the Wanderer Bard"
    def __init__(self):
        super(c383442, self).__init__(gameobject.Characteristics(**{'mana_cost': '2G', 'text': '{2}{G}, {T}, Put a verse counter on Yisan, the Wanderer Bard: Search your library for a creature card with converted mana cost equal to the number of verse counters on Yisan, put it onto the battlefield, then shuffle your library.', 'subtype': ['Human', 'Rogue'], 'power': 2, 'color': ['G'], 'name': 'Yisan, the Wanderer Bard', 'toughness': 3}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383251(card.Card):
    "Garruk, Apex Predator"
    def __init__(self):
        super(c383251, self).__init__(gameobject.Characteristics(**{'mana_cost': '5BG', 'text': '+1: Destroy another target planeswalker.\n+1: Create a 3/3 black Beast creature token with deathtouch.\n−3: Destroy target creature. You gain life equal to its toughness.\n−8: Target opponent gets an emblem with "Whenever a creature attacks you, it gets +5/+5 and gains trample until end of turn."', 'subtype': ['Garruk'], 'name': 'Garruk, Apex Predator', 'color': ['B', 'G']}, supertype=[], types=[cardtype.CardType.PLANESWALKER], abilities=[]))

class c383385(card.Card):
    "Sliver Hivelord"
    def __init__(self):
        super(c383385, self).__init__(gameobject.Characteristics(**{'mana_cost': 'WUBRG', 'text': 'Sliver creatures you control have indestructible. (Damage and effects that say "destroy" don\'t destroy them.)', 'subtype': ['Sliver'], 'power': 5, 'color': ['W', 'U', 'B', 'R', 'G'], 'name': 'Sliver Hivelord', 'toughness': 5}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383186(card.Card):
    "Avarice Amulet"
    def __init__(self):
        super(c383186, self).__init__(gameobject.Characteristics(**{'mana_cost': '4', 'text': 'Equipped creature gets +2/+0 and has vigilance and "At the beginning of your upkeep, draw a card."\nWhenever equipped creature dies, target opponent gains control of Avarice Amulet.\nEquip {2} ({2}: Attach to target creature you control. Equip only as a sorcery.)', 'subtype': ['Equipment'], 'name': 'Avarice Amulet', 'color': ''}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c383196(card.Card):
    "Brawler's Plate"
    def __init__(self):
        super(c383196, self).__init__(gameobject.Characteristics(**{'mana_cost': '3', 'text': 'Equipped creature gets +2/+2 and has trample. (It can deal excess combat damage to defending player or planeswalker while attacking.)\nEquip {4} ({4}: Attach to target creature you control. Equip only as a sorcery.)', 'subtype': ['Equipment'], 'name': "Brawler's Plate", 'color': ''}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c383197(card.Card):
    "Bronze Sable"
    def __init__(self):
        super(c383197, self).__init__(gameobject.Characteristics(**{'mana_cost': '2', 'text': '', 'subtype': ['Sable'], 'power': 2, 'color': '', 'name': 'Bronze Sable', 'toughness': 1}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[]))

class c383412(card.Card):
    "The Chain Veil"
    def __init__(self):
        super(c383412, self).__init__(gameobject.Characteristics(**{'mana_cost': '4', 'text': "At the beginning of your end step, if you didn't activate a loyalty ability of a planeswalker this turn, you lose 2 life.\n{4}, {T}: For each planeswalker you control, you may activate one of its loyalty abilities once this turn as though none of its loyalty abilities have been activated this turn.", 'name': 'The Chain Veil', 'color': ''}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c383250(card.Card):
    "Gargoyle Sentinel"
    def __init__(self):
        super(c383250, self).__init__(gameobject.Characteristics(**{'mana_cost': '3', 'text': "Defender (This creature can't attack.)\n{3}: Until end of turn, Gargoyle Sentinel loses defender and gains flying.", 'subtype': ['Gargoyle'], 'power': 3, 'color': '', 'name': 'Gargoyle Sentinel', 'toughness': 3}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Defender]))

class c383261(card.Card):
    "Grindclock"
    def __init__(self):
        super(c383261, self).__init__(gameobject.Characteristics(**{'mana_cost': '2', 'text': '{T}: Put a charge counter on Grindclock.\n{T}: Target player puts the top X cards of his or her library into his or her graveyard, where X is the number of charge counters on Grindclock.', 'name': 'Grindclock', 'color': ''}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c383263(card.Card):
    "Haunted Plate Mail"
    def __init__(self):
        super(c383263, self).__init__(gameobject.Characteristics(**{'mana_cost': '4', 'text': "Equipped creature gets +4/+4.\n{0}: Until end of turn, Haunted Plate Mail becomes a 4/4 Spirit artifact creature that's no longer an Equipment. Activate this ability only if you control no creatures.\nEquip {4} ({4}: Attach to target creature you control. Equip only as a sorcery.)", 'subtype': ['Equipment'], 'name': 'Haunted Plate Mail', 'color': ''}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c383269(card.Card):
    "Hot Soup"
    def __init__(self):
        super(c383269, self).__init__(gameobject.Characteristics(**{'mana_cost': '1', 'text': "Equipped creature can't be blocked.\nWhenever equipped creature is dealt damage, destroy it.\nEquip {3} ({3}: Attach to target creature you control. Equip only as a sorcery.)", 'subtype': ['Equipment'], 'name': 'Hot Soup', 'color': ''}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c383289(card.Card):
    "Juggernaut"
    def __init__(self):
        super(c383289, self).__init__(gameobject.Characteristics(**{'mana_cost': '4', 'text': "Juggernaut attacks each turn if able.\nJuggernaut can't be blocked by Walls.", 'subtype': ['Juggernaut'], 'power': 5, 'color': '', 'name': 'Juggernaut', 'toughness': 3}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[]))

class c383308(card.Card):
    "Meteorite"
    def __init__(self):
        super(c383308, self).__init__(gameobject.Characteristics(**{'mana_cost': '5', 'text': 'When Meteorite enters the battlefield, it deals 2 damage to target creature or player.\n{T}: Add one mana of any color to your mana pool.', 'name': 'Meteorite', 'color': ''}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c383331(card.Card):
    "Obelisk of Urd"
    def __init__(self):
        super(c383331, self).__init__(gameobject.Characteristics(**{'mana_cost': '6', 'text': "Convoke (Your creatures can help cast this spell. Each creature you tap while casting this spell pays for {1} or one mana of that creature's color.)\nAs Obelisk of Urd enters the battlefield, choose a creature type.\nCreatures you control of the chosen type get +2/+2.", 'name': 'Obelisk of Urd', 'color': ''}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[static_abilities.StaticAbilities.Convoke]))

class c383334(card.Card):
    "Ornithopter"
    def __init__(self):
        super(c383334, self).__init__(gameobject.Characteristics(**{'mana_cost': '0', 'text': 'Flying', 'subtype': ['Thopter'], 'power': 0, 'color': '', 'name': 'Ornithopter', 'toughness': 2}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying]))

class c383342(card.Card):
    "Perilous Vault"
    def __init__(self):
        super(c383342, self).__init__(gameobject.Characteristics(**{'mana_cost': '4', 'text': '{5}, {T}, Exile Perilous Vault: Exile all nonland permanents.', 'name': 'Perilous Vault', 'color': ''}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c383343(card.Card):
    "Phyrexian Revoker"
    def __init__(self):
        super(c383343, self).__init__(gameobject.Characteristics(**{'mana_cost': '2', 'text': "As Phyrexian Revoker enters the battlefield, choose a nonland card name.\nActivated abilities of sources with the chosen name can't be activated.", 'subtype': ['Horror'], 'power': 2, 'color': '', 'name': 'Phyrexian Revoker', 'toughness': 1}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[]))

class c383353(card.Card):
    "Profane Memento"
    def __init__(self):
        super(c383353, self).__init__(gameobject.Characteristics(**{'mana_cost': '1', 'text': "Whenever a creature card is put into an opponent's graveyard from anywhere, you gain 1 life.", 'name': 'Profane Memento', 'color': ''}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c383365(card.Card):
    "Rogue's Gloves"
    def __init__(self):
        super(c383365, self).__init__(gameobject.Characteristics(**{'mana_cost': '2', 'text': 'Whenever equipped creature deals combat damage to a player, you may draw a card.\nEquip {2} ({2}: Attach to target creature you control. Equip only as a sorcery.)', 'subtype': ['Equipment'], 'name': "Rogue's Gloves", 'color': ''}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c383369(card.Card):
    "Sacred Armory"
    def __init__(self):
        super(c383369, self).__init__(gameobject.Characteristics(**{'mana_cost': '2', 'text': '{2}: Target creature gets +1/+0 until end of turn.', 'name': 'Sacred Armory', 'color': ''}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c383373(card.Card):
    "Scuttling Doom Engine"
    def __init__(self):
        super(c383373, self).__init__(gameobject.Characteristics(**{'mana_cost': '6', 'text': "Scuttling Doom Engine can't be blocked by creatures with power 2 or less.\nWhen Scuttling Doom Engine dies, it deals 6 damage to target opponent.", 'subtype': ['Construct'], 'power': 6, 'color': '', 'name': 'Scuttling Doom Engine', 'toughness': 6}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[]))

class c383378(card.Card):
    "Shield of the Avatar"
    def __init__(self):
        super(c383378, self).__init__(gameobject.Characteristics(**{'mana_cost': '1', 'text': 'If a source would deal damage to equipped creature, prevent X of that damage, where X is the number of creatures you control.\nEquip {2} ({2}: Attach to target creature you control. Equip only as a sorcery.)', 'subtype': ['Equipment'], 'name': 'Shield of the Avatar', 'color': ''}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c383388(card.Card):
    "Soul of New Phyrexia"
    def __init__(self):
        super(c383388, self).__init__(gameobject.Characteristics(**{'mana_cost': '6', 'text': 'Trample\n{5}: Permanents you control gain indestructible until end of turn.\n{5}, Exile Soul of New Phyrexia from your graveyard: Permanents you control gain indestructible until end of turn.', 'subtype': ['Avatar'], 'power': 6, 'color': '', 'name': 'Soul of New Phyrexia', 'toughness': 6}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Trample]))

class c383397(card.Card):
    "Staff of the Death Magus"
    def __init__(self):
        super(c383397, self).__init__(gameobject.Characteristics(**{'mana_cost': '3', 'text': 'Whenever you cast a black spell or a Swamp enters the battlefield under your control, you gain 1 life.', 'name': 'Staff of the Death Magus', 'color': ''}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c383398(card.Card):
    "Staff of the Flame Magus"
    def __init__(self):
        super(c383398, self).__init__(gameobject.Characteristics(**{'mana_cost': '3', 'text': 'Whenever you cast a red spell or a Mountain enters the battlefield under your control, you gain 1 life.', 'name': 'Staff of the Flame Magus', 'color': ''}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c383399(card.Card):
    "Staff of the Mind Magus"
    def __init__(self):
        super(c383399, self).__init__(gameobject.Characteristics(**{'mana_cost': '3', 'text': 'Whenever you cast a blue spell or an Island enters the battlefield under your control, you gain 1 life.', 'name': 'Staff of the Mind Magus', 'color': ''}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c383400(card.Card):
    "Staff of the Sun Magus"
    def __init__(self):
        super(c383400, self).__init__(gameobject.Characteristics(**{'mana_cost': '3', 'text': 'Whenever you cast a white spell or a Plains enters the battlefield under your control, you gain 1 life.', 'name': 'Staff of the Sun Magus', 'color': ''}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c383401(card.Card):
    "Staff of the Wild Magus"
    def __init__(self):
        super(c383401, self).__init__(gameobject.Characteristics(**{'mana_cost': '3', 'text': 'Whenever you cast a green spell or a Forest enters the battlefield under your control, you gain 1 life.', 'name': 'Staff of the Wild Magus', 'color': ''}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c383417(card.Card):
    "Tormod's Crypt"
    def __init__(self):
        super(c383417, self).__init__(gameobject.Characteristics(**{'mana_cost': '0', 'text': "{T}, Sacrifice Tormod's Crypt: Exile all cards from target player's graveyard.", 'name': "Tormod's Crypt", 'color': ''}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c383421(card.Card):
    "Tyrant's Machine"
    def __init__(self):
        super(c383421, self).__init__(gameobject.Characteristics(**{'mana_cost': '2', 'text': '{4}, {T}: Tap target creature.', 'name': "Tyrant's Machine", 'color': ''}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c383438(card.Card):
    "Will-Forged Golem"
    def __init__(self):
        super(c383438, self).__init__(gameobject.Characteristics(**{'mana_cost': '6', 'text': "Convoke (Your creatures can help cast this spell. Each creature you tap while casting this spell pays for {1} or one mana of that creature's color.)", 'subtype': ['Golem'], 'power': 4, 'color': '', 'name': 'Will-Forged Golem', 'toughness': 4}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Convoke]))

class c383189(card.Card):
    "Battlefield Forge"
    def __init__(self):
        super(c383189, self).__init__(gameobject.Characteristics(**{'mana_cost': '', 'text': '{T}: Add {C} to your mana pool.\n{T}: Add {R} or {W} to your mana pool. Battlefield Forge deals 1 damage to you.', 'name': 'Battlefield Forge', 'color': ['R', 'W']}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c383203(card.Card):
    "Caves of Koilos"
    def __init__(self):
        super(c383203, self).__init__(gameobject.Characteristics(**{'mana_cost': '', 'text': '{T}: Add {C} to your mana pool.\n{T}: Add {W} or {B} to your mana pool. Caves of Koilos deals 1 damage to you.', 'name': 'Caves of Koilos', 'color': ['W', 'B']}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c383222(card.Card):
    "Darksteel Citadel"
    def __init__(self):
        super(c383222, self).__init__(gameobject.Characteristics(**{'mana_cost': '', 'text': 'Indestructible\n{T}: Add {C} to your mana pool.', 'name': 'Darksteel Citadel', 'color': ''}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.LAND], abilities=[static_abilities.StaticAbilities.Indestructible]))

class c383235(card.Card):
    "Evolving Wilds"
    def __init__(self):
        super(c383235, self).__init__(gameobject.Characteristics(**{'mana_cost': '', 'text': '{T}, Sacrifice Evolving Wilds: Search your library for a basic land card and put it onto the battlefield tapped. Then shuffle your library.', 'name': 'Evolving Wilds', 'color': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c383302(card.Card):
    "Llanowar Wastes"
    def __init__(self):
        super(c383302, self).__init__(gameobject.Characteristics(**{'mana_cost': '', 'text': '{T}: Add {C} to your mana pool.\n{T}: Add {B} or {G} to your mana pool. Llanowar Wastes deals 1 damage to you.', 'name': 'Llanowar Wastes', 'color': ['B', 'G']}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c383355(card.Card):
    "Radiant Fountain"
    def __init__(self):
        super(c383355, self).__init__(gameobject.Characteristics(**{'mana_cost': '', 'text': 'When Radiant Fountain enters the battlefield, you gain 2 life.\n{T}: Add {C} to your mana pool.', 'name': 'Radiant Fountain', 'color': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c383379(card.Card):
    "Shivan Reef"
    def __init__(self):
        super(c383379, self).__init__(gameobject.Characteristics(**{'mana_cost': '', 'text': '{T}: Add {C} to your mana pool.\n{T}: Add {U} or {R} to your mana pool. Shivan Reef deals 1 damage to you.', 'name': 'Shivan Reef', 'color': ['U', 'R']}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c383384(card.Card):
    "Sliver Hive"
    def __init__(self):
        super(c383384, self).__init__(gameobject.Characteristics(**{'mana_cost': '', 'text': '{T}: Add {C} to your mana pool.\n{T}: Add one mana of any color to your mana pool. Spend this mana only to cast a Sliver spell.\n{5}, {T}: Create a 1/1 colorless Sliver creature token. Activate this ability only if you control a Sliver.', 'name': 'Sliver Hive', 'color': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c383425(card.Card):
    "Urborg, Tomb of Yawgmoth"
    def __init__(self):
        super(c383425, self).__init__(gameobject.Characteristics(**{'mana_cost': '', 'text': 'Each land is a Swamp in addition to its other land types.', 'name': 'Urborg, Tomb of Yawgmoth', 'color': ''}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.LAND], abilities=[]))

class c383441(card.Card):
    "Yavimaya Coast"
    def __init__(self):
        super(c383441, self).__init__(gameobject.Characteristics(**{'mana_cost': '', 'text': '{T}: Add {C} to your mana pool.\n{T}: Add {G} or {U} to your mana pool. Yavimaya Coast deals 1 damage to you.', 'name': 'Yavimaya Coast', 'color': ['G', 'U']}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c383347(card.Card):
    "Plains"
    def __init__(self):
        super(c383347, self).__init__(gameobject.Characteristics(**{'mana_cost': '', 'text': '', 'subtype': ['Plains'], 'name': 'Plains', 'color': ['W']}, supertype=[cardtype.SuperType.BASIC], types=[cardtype.CardType.LAND], abilities=[]))

class c383346(card.Card):
    "Plains"
    def __init__(self):
        super(c383346, self).__init__(gameobject.Characteristics(**{'mana_cost': '', 'text': '', 'subtype': ['Plains'], 'name': 'Plains', 'color': ['W']}, supertype=[cardtype.SuperType.BASIC], types=[cardtype.CardType.LAND], abilities=[]))

class c383348(card.Card):
    "Plains"
    def __init__(self):
        super(c383348, self).__init__(gameobject.Characteristics(**{'mana_cost': '', 'text': '', 'subtype': ['Plains'], 'name': 'Plains', 'color': ['W']}, supertype=[cardtype.SuperType.BASIC], types=[cardtype.CardType.LAND], abilities=[]))

class c383349(card.Card):
    "Plains"
    def __init__(self):
        super(c383349, self).__init__(gameobject.Characteristics(**{'mana_cost': '', 'text': '', 'subtype': ['Plains'], 'name': 'Plains', 'color': ['W']}, supertype=[cardtype.SuperType.BASIC], types=[cardtype.CardType.LAND], abilities=[]))

class c383284(card.Card):
    "Island"
    def __init__(self):
        super(c383284, self).__init__(gameobject.Characteristics(**{'mana_cost': '', 'text': '', 'subtype': ['Island'], 'name': 'Island', 'color': ['U']}, supertype=[cardtype.SuperType.BASIC], types=[cardtype.CardType.LAND], abilities=[]))

class c383281(card.Card):
    "Island"
    def __init__(self):
        super(c383281, self).__init__(gameobject.Characteristics(**{'mana_cost': '', 'text': '', 'subtype': ['Island'], 'name': 'Island', 'color': ['U']}, supertype=[cardtype.SuperType.BASIC], types=[cardtype.CardType.LAND], abilities=[]))

class c383283(card.Card):
    "Island"
    def __init__(self):
        super(c383283, self).__init__(gameobject.Characteristics(**{'mana_cost': '', 'text': '', 'subtype': ['Island'], 'name': 'Island', 'color': ['U']}, supertype=[cardtype.SuperType.BASIC], types=[cardtype.CardType.LAND], abilities=[]))

class c383282(card.Card):
    "Island"
    def __init__(self):
        super(c383282, self).__init__(gameobject.Characteristics(**{'mana_cost': '', 'text': '', 'subtype': ['Island'], 'name': 'Island', 'color': ['U']}, supertype=[cardtype.SuperType.BASIC], types=[cardtype.CardType.LAND], abilities=[]))

class c383409(card.Card):
    "Swamp"
    def __init__(self):
        super(c383409, self).__init__(gameobject.Characteristics(**{'mana_cost': '', 'text': '', 'subtype': ['Swamp'], 'name': 'Swamp', 'color': ['B']}, supertype=[cardtype.SuperType.BASIC], types=[cardtype.CardType.LAND], abilities=[]))

class c383410(card.Card):
    "Swamp"
    def __init__(self):
        super(c383410, self).__init__(gameobject.Characteristics(**{'mana_cost': '', 'text': '', 'subtype': ['Swamp'], 'name': 'Swamp', 'color': ['B']}, supertype=[cardtype.SuperType.BASIC], types=[cardtype.CardType.LAND], abilities=[]))

class c383411(card.Card):
    "Swamp"
    def __init__(self):
        super(c383411, self).__init__(gameobject.Characteristics(**{'mana_cost': '', 'text': '', 'subtype': ['Swamp'], 'name': 'Swamp', 'color': ['B']}, supertype=[cardtype.SuperType.BASIC], types=[cardtype.CardType.LAND], abilities=[]))

class c383408(card.Card):
    "Swamp"
    def __init__(self):
        super(c383408, self).__init__(gameobject.Characteristics(**{'mana_cost': '', 'text': '', 'subtype': ['Swamp'], 'name': 'Swamp', 'color': ['B']}, supertype=[cardtype.SuperType.BASIC], types=[cardtype.CardType.LAND], abilities=[]))

class c383315(card.Card):
    "Mountain"
    def __init__(self):
        super(c383315, self).__init__(gameobject.Characteristics(**{'mana_cost': '', 'text': '', 'subtype': ['Mountain'], 'name': 'Mountain', 'color': ['R']}, supertype=[cardtype.SuperType.BASIC], types=[cardtype.CardType.LAND], abilities=[]))

class c383317(card.Card):
    "Mountain"
    def __init__(self):
        super(c383317, self).__init__(gameobject.Characteristics(**{'mana_cost': '', 'text': '', 'subtype': ['Mountain'], 'name': 'Mountain', 'color': ['R']}, supertype=[cardtype.SuperType.BASIC], types=[cardtype.CardType.LAND], abilities=[]))

class c383318(card.Card):
    "Mountain"
    def __init__(self):
        super(c383318, self).__init__(gameobject.Characteristics(**{'mana_cost': '', 'text': '', 'subtype': ['Mountain'], 'name': 'Mountain', 'color': ['R']}, supertype=[cardtype.SuperType.BASIC], types=[cardtype.CardType.LAND], abilities=[]))

class c383316(card.Card):
    "Mountain"
    def __init__(self):
        super(c383316, self).__init__(gameobject.Characteristics(**{'mana_cost': '', 'text': '', 'subtype': ['Mountain'], 'name': 'Mountain', 'color': ['R']}, supertype=[cardtype.SuperType.BASIC], types=[cardtype.CardType.LAND], abilities=[]))

class c383244(card.Card):
    "Forest"
    def __init__(self):
        super(c383244, self).__init__(gameobject.Characteristics(**{'mana_cost': '', 'text': '', 'subtype': ['Forest'], 'name': 'Forest', 'color': ['G']}, supertype=[cardtype.SuperType.BASIC], types=[cardtype.CardType.LAND], abilities=[]))

class c383242(card.Card):
    "Forest"
    def __init__(self):
        super(c383242, self).__init__(gameobject.Characteristics(**{'mana_cost': '', 'text': '', 'subtype': ['Forest'], 'name': 'Forest', 'color': ['G']}, supertype=[cardtype.SuperType.BASIC], types=[cardtype.CardType.LAND], abilities=[]))

class c383243(card.Card):
    "Forest"
    def __init__(self):
        super(c383243, self).__init__(gameobject.Characteristics(**{'mana_cost': '', 'text': '', 'subtype': ['Forest'], 'name': 'Forest', 'color': ['G']}, supertype=[cardtype.SuperType.BASIC], types=[cardtype.CardType.LAND], abilities=[]))

class c383241(card.Card):
    "Forest"
    def __init__(self):
        super(c383241, self).__init__(gameobject.Characteristics(**{'mana_cost': '', 'text': '', 'subtype': ['Forest'], 'name': 'Forest', 'color': ['G']}, supertype=[cardtype.SuperType.BASIC], types=[cardtype.CardType.LAND], abilities=[]))

class c383160(card.Card):
    "Aegis Angel"
    def __init__(self):
        super(c383160, self).__init__(gameobject.Characteristics(**{'mana_cost': '4WW', 'text': 'Flying (This creature can\'t be blocked except by creatures with flying or reach.)\nWhen Aegis Angel enters the battlefield, another target permanent gains indestructible for as long as you control Aegis Angel. (Effects that say "destroy" don\'t destroy it. A creature with indestructible can\'t be destroyed by damage.)', 'subtype': ['Angel'], 'power': 5, 'color': ['W'], 'name': 'Aegis Angel', 'toughness': 5}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying]))

class c383163(card.Card):
    "Divine Verdict"
    def __init__(self):
        super(c383163, self).__init__(gameobject.Characteristics(**{'mana_cost': '3W', 'text': 'Destroy target attacking or blocking creature.', 'name': 'Divine Verdict', 'color': ['W']}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c383166(card.Card):
    "Inspired Charge"
    def __init__(self):
        super(c383166, self).__init__(gameobject.Characteristics(**{'mana_cost': '2WW', 'text': 'Creatures you control get +2/+1 until end of turn.', 'name': 'Inspired Charge', 'color': ['W']}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c383171(card.Card):
    "Serra Angel"
    def __init__(self):
        super(c383171, self).__init__(gameobject.Characteristics(**{'mana_cost': '3WW', 'text': "Flying (This creature can't be blocked except by creatures with flying or reach.)\nVigilance (Attacking doesn't cause this creature to tap.)", 'subtype': ['Angel'], 'power': 4, 'color': ['W'], 'name': 'Serra Angel', 'toughness': 4}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying, static_abilities.StaticAbilities.Vigilance]))

class c383161(card.Card):
    "Cancel"
    def __init__(self):
        super(c383161, self).__init__(gameobject.Characteristics(**{'mana_cost': '1UU', 'text': 'Counter target spell.', 'name': 'Cancel', 'color': ['U']}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c383167(card.Card):
    "Mahamoti Djinn"
    def __init__(self):
        super(c383167, self).__init__(gameobject.Characteristics(**{'mana_cost': '4UU', 'text': "Flying (This creature can't be blocked except by creatures with flying or reach.)", 'subtype': ['Djinn'], 'power': 5, 'color': ['U'], 'name': 'Mahamoti Djinn', 'toughness': 6}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying]))

class c383168(card.Card):
    "Nightmare"
    def __init__(self):
        super(c383168, self).__init__(gameobject.Characteristics(**{'mana_cost': '5B', 'text': "Flying (This creature can't be blocked except by creatures with flying or reach.)\nNightmare's power and toughness are each equal to the number of Swamps you control.", 'subtype': ['Nightmare', 'Horse'], 'power': '*', 'color': ['B'], 'name': 'Nightmare', 'toughness': '*'}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying]))

class c383170(card.Card):
    "Sengir Vampire"
    def __init__(self):
        super(c383170, self).__init__(gameobject.Characteristics(**{'mana_cost': '3BB', 'text': "Flying (This creature can't be blocked except by creatures with flying or reach.)\nWhenever a creature dealt damage by Sengir Vampire this turn dies, put a +1/+1 counter on Sengir Vampire.", 'subtype': ['Vampire'], 'power': 4, 'color': ['B'], 'name': 'Sengir Vampire', 'toughness': 4}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying]))

class c383174(card.Card):
    "Walking Corpse"
    def __init__(self):
        super(c383174, self).__init__(gameobject.Characteristics(**{'mana_cost': '1B', 'text': '', 'subtype': ['Zombie'], 'power': 2, 'color': ['B'], 'name': 'Walking Corpse', 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383164(card.Card):
    "Furnace Whelp"
    def __init__(self):
        super(c383164, self).__init__(gameobject.Characteristics(**{'mana_cost': '2RR', 'text': "Flying (This creature can't be blocked except by creatures with flying or reach.)\n{R}: Furnace Whelp gets +1/+0 until end of turn.", 'subtype': ['Dragon'], 'power': 2, 'color': ['R'], 'name': 'Furnace Whelp', 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying]))

class c383169(card.Card):
    "Seismic Strike"
    def __init__(self):
        super(c383169, self).__init__(gameobject.Characteristics(**{'mana_cost': '2R', 'text': 'Seismic Strike deals damage to target creature equal to the number of Mountains you control.', 'name': 'Seismic Strike', 'color': ['R']}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c383172(card.Card):
    "Shivan Dragon"
    def __init__(self):
        super(c383172, self).__init__(gameobject.Characteristics(**{'mana_cost': '4RR', 'text': "Flying (This creature can't be blocked except by creatures with flying or reach.)\n{R}: Shivan Dragon gets +1/+0 until end of turn.", 'subtype': ['Dragon'], 'power': 5, 'color': ['R'], 'name': 'Shivan Dragon', 'toughness': 5}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying]))

class c383162(card.Card):
    "Centaur Courser"
    def __init__(self):
        super(c383162, self).__init__(gameobject.Characteristics(**{'mana_cost': '2G', 'text': '', 'subtype': ['Centaur', 'Warrior'], 'power': 3, 'color': ['G'], 'name': 'Centaur Courser', 'toughness': 3}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383165(card.Card):
    "Garruk's Packleader"
    def __init__(self):
        super(c383165, self).__init__(gameobject.Characteristics(**{'mana_cost': '4G', 'text': 'Whenever another creature with power 3 or greater enters the battlefield under your control, you may draw a card.', 'subtype': ['Beast'], 'power': 4, 'color': ['G'], 'name': "Garruk's Packleader", 'toughness': 4}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383173(card.Card):
    "Terra Stomper"
    def __init__(self):
        super(c383173, self).__init__(gameobject.Characteristics(**{'mana_cost': '3GGG', 'text': "Terra Stomper can't be countered.\nTrample (This creature can deal excess combat damage to defending player or planeswalker while attacking.)", 'subtype': ['Beast'], 'power': 8, 'color': ['G'], 'name': 'Terra Stomper', 'toughness': 8}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Trample]))

