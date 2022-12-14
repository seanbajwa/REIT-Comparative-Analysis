from secedgar import filings, FilingType

# 10Q filings for Apple and Facebook (tickers from REIT List Garrett wanted)
my_filings = filings(cik_lookup=["ABR",	"ACR",	"ACRE",	"AGNC",	"AJX",	"AOMR",	"ARI",	"ARR",	"BRMK",	"BXMT",	"CHMI",	"CIM",	"CMTG",	"DX",	"EARN",	"EFC",	"GPMT",	"HASI",	"IVR",	"KREF",	"LADR",	"LFT",	"LOAN",	"MFA",	"MITT",	"NLY",	"NREF",	"NRZ",	"NYMT",	"ORC",	"PMT",	"RC",	"REFI",	"RWT",	"SACH",	"STAR",	"STWD",	"TRTX",	"TWO",	"WMC",
],
                     filing_type=FilingType.FILING_10Q,
                     user_agent="Your name (your email)")
my_filings.save(r"C:\Users\sbajwa\Box\Syndication\Market Landscape\Bajwa Code\Edgar")