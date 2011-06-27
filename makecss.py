from itertools import izip
#why? Because I'm fuckin' lazy

#colors all stolen from Gmail
colors = """dee4f3/6e7898
dfebff/5166ff
e1dfff/4b00da
e5d0fc/7615b5
ffe6f4/9f5f77
ffe1e2/e30005
5a6688/c9d1e2
4646ff/c2d4ff
4000d3/c1b7fb
6300a8/d1b2ee
8d4761/efcedd
dc0000/ffbcbf
fff1df/fa7f00
fddeae/c47e00
f2ebad/767e43
f7ffee/64b13b
fa6800/ffddba
ba6c00/f2cd90
ac9000/e5dd8f
5f6728/e4ebb6
48a20f/ddf3cf
006c2e/c7e2ce
c7e2ce/006c2e
"""

#these are all the classes, astute observers will note that there are more of them than there are color combos.
classes = """online-computer-services
accident-health-insurance
commercial-banks
transportation
water-utilities
engineering-architecture-construction-mgmt-svcs
other-single-issue-or-ideological-groups
fisheries-wildlife
private-equity-investment-firms
home-builders
abortion-policypro-choice
other-non-physician-health-practitioners
forestry-forest-products
accountants
indian-gaming
republican-based-groups-but-not-official-party-committees-and-generic-conservative-ones
alternate-energy-production-services
pro-israel
civil-servantspublic-officials
hotels-motels
health-care-services
other-financial-services
misc-energy
entertainment-industrybroadcast-motion-pictures
venture-capital
misc-business
public-school-teachers-administrators-officials
electric-utilities
engineers-type-unknown
fiscal-tax-policy
lobbyists
clergy-religious-organizations
computer-manufacture-services
telecommunications
abortion-policypro-life
medical-schools
tvmoviesmusic
misc-defense
trucking
recycling-of-metal-paper-plastics-etc
financecredit-companies
nonpartisan-elected-officials-candidates
pharmaceutical-manufacturing
department-variety-convenience-stores
leadership-pacs
environmental-policy
metal-mining-processing
health-professionals
business-services
meat-processing-products
building-trade-unions
womens-issues
non-profit-institutions
retired
defense-policy-hawks
professional-sports-arenas-related-equip-svcs
schools-colleges
native-american-tribes-governing-units
household-appliances
misc-services
securities-commodities-investment
electric-power-utilities
oil-gas
agricultural-servicesproducts
marketing-research-services
democraticliberal
childrens-rights
education
warehousing
lawyerslaw-firms
cruise-ships-lines
unknown
livestock
employer-listed-but-category-unknown
insurance
chambers-of-commerce
printing-publishing
waste-management"""

color_array = []
class_array = []
colors = colors.split("\n")
for color in colors:
    color_array.append(color.split("/"))
class_array = classes.split("\n")

for color, classs in izip(color_array,class_array):
    print(""".%s {
    background-color:#%s;
    color:#%s;
    border-color:#%s
}"""%(classs, color[0], color[1], color[1]))
