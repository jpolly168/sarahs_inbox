from itertools import izip
#why? Because I'm fuckin' lazy

#colors all stolen from Gmail
colors = """dee4f3/6e7898
dfebff/5166ff
e1dfff/4b00da
e5d0fc/7615b5
ffe6f4/9f5f77
ffe1e2/e30005
046380/ffffff
002f2f/ffffff
382513/ffffff
8e2800/ffffff
468966/ffffff
d8caa8/382513
836527/ffffff
aa835a/ffffff
055995/ffffff
7a8ec3/ffffff
097dc8/ffffff
042842/ffffff
c7a79a/383839
fde9f2/383839
e4c6ce/383839
a89d8b/ffffff
695a5f/ffffff
383839/ffffff
7c92b7/ffffff
968b93/ffffff
a78353/ffffff
f5ceaf/383839
eadfff/383839
ffefff/383839
ffd893/383839
ecbfa2/383839
f2c077/383839
fabc33/ffffff
d4ac57/ffffff
a28162/ffffff
d7d7d7/333333
a1a1a1/ffffff
7d7d7d/ffffff
555555/ffffff
363636/ffffff
000000/ffffff
f4d67e/3180cf
ffd078/3180cf
ffda77/3180cf
f0c193/3180cf
e3a924/fbeafc
e0a24f/fbeafc
cccccc/6f6065
cccccc/6a4b08
cccccc/a67e00
cccccc/5c679f
cccccc/043a66
cccccc/3180cf
093969/e3a038
093969/e8ddff
093969/a59e8e
093969/ffd493
093969/e1c5d3
093969/ffffff
e0c5cc/ffffff
e0c5cc/ac8800
e0c5cc/6d6165
e0c5cc/067add
e0c5cc/5680ba
e0c5cc/00609e
629df7/00ffff
629df7/ffe5ee
629df7/fed6a5
629df7/bedb39
629df7/00446b
629df7/625004
6e590a/87a1f8
6e590a/e9a230
6e590a/bedb39
6e590a/fed6a5
6e590a/ffe5ee
6e590a/00ffff
"""

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
