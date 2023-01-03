# REIT-Comparative-Analysis

Shareholder Activism Research for Competitive Analyses against Competing REITs (Blackstone, KKR, Starwood and more).
from sec_edgar_downloader import Downloader
 #### My idol is Paul Singer, Elliott Management an alumni of the University of Rochester (my alma mater for undergraduate studies in 2018).


Add files via upload
-------Main Edgr 10Q Compiler.py Code Usage Below
from sec_edgar_downloader import Downloader

# Initialize a downloader instance. If no argument is passed
# to the constructor, the package will download filings to
# the current working directory.
dl = Downloader("/path/to/valid/save/location")

# Get all 8-K filings for Apple (ticker: STWD)
dl.get("8-K", "STWD")

# Get all 8-K filings for Apple, including filing amends (8-K/A)
dl.get("8-K", "STWD", include_amends=True)

# Get all 8-K filings for Apple after January 1, 2020 and before March 25, 2020
# Note: after and before strings must be in the form "YYYY-MM-DD"
dl.get("8-K", "STWD", after="2020-01-01", before="2020-03-25")

# Get the five most recent 8-K filings for Starwood
dl.get("8-K", "STWD", amount=5)

# Get all 10-K filings for Starwood
dl.get("10-K", "STWD")

# Get the latest 10-K filing for Starwood
dl.get("10-K", "STWD", amount=1)

# Get all 10-Q filings for Starwood
dl.get("10-Q", "STWD")

# Get all 13F-NT filings for Starwood
dl.get("13F-NT", "0000102909")

# Get all 13F-HR filings for Starwood
dl.get("13F-HR", "0000102909")

# Get all SC 13G filings for Starwood
dl.get("SC 13G", "STWD")

# Get all SD filings for Starwood
dl.get("SD", "STWD")

_____________________________________________________________________________

Shareholder Activism Research for Competitive Analyses against Competing REITs (Blackstone, KKR, Starwood and more).
from sec_edgar_downloader import Downloader
 #### My idol is Paul Singer, Elliott Management an alumni of the University of Rochester (my alma mater for undergraduate studies in 2018).

# Download filings to the current working directory
dl = Downloader()

# Get all Apple proxy statements that contain the term "antitrust"
dl.get("DEF 14A", "STWD", query="antitrust")

# Get all 10-K filings for Microsoft without the filing details
dl.get("10-K", "STWD", download_details=False)

# Get the latest supported filings, if available, for Starwood
for filing_type in dl.supported_filings:
    dl.get(filing_type, "STWD", amount=1)

# Get the latest supported filings, if available, for a
# specified list of tickers and CIKs
equity_ids = ["STWD", "0000102909", "KREF", "BXMT"]
for equity_id in equity_ids:
    for filing_type in dl.supported_filings:
        dl.get(filing_type, equity_id, amount=1)
_______________________________________________

####Vba code helps file map your list.xlsx (alt +f11 and add module of vba script) 
#list.xlsx add as many names as you like and for loop will create in your selected folder path.
# Python REIT List are the most important REITs arguably in 2022 based on Competitive Market Analysis Prop Research owned by ACORE Capital (all rights reserved)

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

