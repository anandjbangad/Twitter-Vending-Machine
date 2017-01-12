#Twitter Vending Machine
from temboo.Library.Twitter.DirectMessages import SendDirectMessage
from temboo.core.session import TembooSession
from temboo.Library.Twitter.Timelines import LatestMention
from temboo.core.session import TembooSession
import random
import urllib
rand_num = random.randint(2000,5000)
# Create a session with your Temboo account details
session = TembooSession("anandjbangad", "myFirstApp", "2fb5SR7S5rXwoBBNc4hK9QJvfeq1LHg4")
latestMentionChoreo = LatestMention(session)
latestMentionInputs = latestMentionChoreo.new_input_set()
# Instantiate the Choreo
sendDirectMessageChoreo = SendDirectMessage(session)
url = "http://www.anandbangad.com/codewrite.php?code="
# Get an InputSet object for the Choreo
sendDirectMessageInputs = sendDirectMessageChoreo.new_input_set()

latestMentionInputs.set_ConsumerKey("8KMFkb3BxAUteOHVxdtavs2jy")
latestMentionInputs.set_AccessToken("2549604530-CwKCLmFLpyJxeb2kS1ddAS6QnRRN9AXH1BiInXc")
latestMentionInputs.set_ConsumerSecret("vy1pYfVVtUut7dRqmkMj9v3MkBkBME8Ib4tllWqGQl936dPN54")
latestMentionInputs.set_AccessTokenSecret("mhwBhp5Xz4gjX6wRbvm8MIAMDFxszVcgTPUovUwjqwmmh")

# Execute the Choreo
latestMentionResults = latestMentionChoreo.execute_with_results(latestMentionInputs)

# Print the Choreo outputs
print("ID: " + latestMentionResults.get_ID())
print("Limit: " + latestMentionResults.get_Limit())
print("Remaining: " + latestMentionResults.get_Remaining())
print("Reset: " + latestMentionResults.get_Reset())
print("ScreenName: " + latestMentionResults.get_ScreenName())
print("Text: " + latestMentionResults.get_Text())

# Set the Choreo inputs
sendDirectMessageInputs.set_ConsumerKey("8KMFkb3BxAUteOHVxdtavs2jy")
sendDirectMessageInputs.set_UserID(str(latestMentionResults.get_ID()))
sendDirectMessageInputs.set_AccessToken("2549604530-CwKCLmFLpyJxeb2kS1ddAS6QnRRN9AXH1BiInXc")
sendDirectMessageInputs.set_ConsumerSecret("vy1pYfVVtUut7dRqmkMj9v3MkBkBME8Ib4tllWqGQl936dPN54")
sendDirectMessageInputs.set_ScreenName(str(latestMentionResults.get_ScreenName()))
sendDirectMessageInputs.set_AccessTokenSecret("mhwBhp5Xz4gjX6wRbvm8MIAMDFxszVcgTPUovUwjqwmmh")
sendDirectMessageInputs.set_Text("Your random code is" +" " + str(rand_num))

# Execute the Choreo
sendDirectMessageResults = sendDirectMessageChoreo.execute_with_results(sendDirectMessageInputs)

# Print the Choreo outputs
#print("Response: " + sendDirectMessageResults.get_Response())
url_code = url + str(rand_num)
response = urlib.urlopen(url_code).read()







# Create a session with your Temboo account details

# Instantiate the Choreo

# Get an InputSet object for the Choreo


# Set the Choreo inputs
#print("Response: " + latestMentionResults.get_Response())
