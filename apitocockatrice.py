from pokemontcgsdk import Card
from pokemontcgsdk import Set
from pokemontcgsdk import Type
from pokemontcgsdk import Supertype
from pokemontcgsdk import Subtype
from pokemontcgsdk import Rarity

from pokemontcgsdk import RestClient

RestClient.configure('d1d4d767-2e9b-4616-a09a-b82ecb6cb43b')

cards = Card.where(q='legalities.standard:legal')
#cards = Card.where(q='legalities.expanded:banned')
#cards = Card.where(q='name:weedle')
print(cards[1])
totaltxt = ""
cardtext = ""
#Pokémon
#Rules is the name for trainer text
for card in cards:
    cardtext = ""
    if card.supertype == "Pokémon":
        try:
            cardtext = "Abilities: "
            abilitytext = card.abilities[0].name + ": " + card.abilities[0].text
            cardtext = cardtext + abilitytext
        except: pass
        try:
            cardtext = cardtext + " Attacks: "
            for attack in card.attacks:
                energycost = ": Energy Cost:"
                for cost in attack.cost:
                    energycost = energycost + cost + ", "
                if not attack.damage:
                    damagetext = "No Damage, "
                else:
                    damagetext = attack.damage
                attacktext = attack.name + energycost + damagetext + attack.text + " "
                cardtext = cardtext + attacktext
        except: pass
    else:
        try:
            for i in card.rules:
                cardtext = cardtext + i + " "
        except: pass
        
    carddata = """
    <card>
        <name>{name}</name>
        <text>{text}</text>
        <prop>
            <type>{supertype}</type>
            <side>front</side>
    </prop>
        <set num="79949" uuid="bdde2617-2c9f-4838-bba7-a60b0f2b5529" rarity="uncommon" picurl="{image}">PKM</set>
        <tablerow>1</tablerow>
        <cipt>1</cipt>
    </card>
    """
    carddata = carddata.format(name = card.name, text = cardtext, supertype = card.supertype, image = card.images.large)
    totaltxt = totaltxt + carddata
encodedtxt = totaltxt.encode("utf8")
with open("cardstext.txt", "wb") as f:
    f.write(encodedtxt)

#<card>
#    <name>Battle VIP Pass</name>
#    <text>When Treacherous Blessing enters the battlefield, draw three cards.
#    Whenever you cast a spell, you lose 1 life.
#    When Treacherous Blessing becomes the target of a spell or ability, sacrifice it.</text>
#    <prop>
#        <type>Trainer</type>
#        <side>front</side>
#   </prop>
#    <set num="79949" uuid="bdde2617-2c9f-4838-bba7-a60b0f2b5529" rarity="uncommon">PKM</set>
#    <tablerow>1</tablerow>
#</card>
