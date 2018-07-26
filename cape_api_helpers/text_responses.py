# Text to show the api users
INVALID_CREDENTIALS_TEXT = 'Invalid credentials supplied'
VALID_CREDENTIALS_TEXT = 'Valid credentials supplied'
LOGGED_OUT_TEXT = 'User logged out'
NOT_LOGGED_TEXT = 'This operation needs authentication. Please ensure that you have either logged in or that you are using the adminToken parameter.'
TIMEOUT_TEXT = 'Operation took longer than anticipated and was aborted.'
NOT_FOUND_TEXT = 'Could not find the resources to execute the operation.'
INVALID_TOKEN = "Token '%s' does not exist."
INVALID_DOC_ID = "One or more documents in '%s' do not exist."
ADMIN_ONLY = "This functionality is only available to administrators."
ERROR_INVALID_PLAN = "The plan provided is invalid got : %s  was expecting : %s"
ERROR_MAX_SIZE_INLINE_TEXT = "This endpoint accepts text of at most %d characters but got %d"
ERROR_TEXT = 'Something went wrong while processing the request.'
ERROR_NUMERIC_REQUIRED = "Parameter '%s' requires a numeric value."
ERROR_TRUE_FALSE_BOTH_REQUIRED = "Parameter '%s' requires a value of either 'true', 'false' or 'both'."
ERROR_REQUIRED_PARAMETER = "The parameter '%s' must be set for this request."
ERROR_INBOX_DOES_NOT_EXIST = "Inbox item '%s' does not exist."
ERROR_DOCUMENT_ALREADY_EXISTS = "A document with the ID '%s' already exists. To replace this document please specify 'replace=true'."
ERROR_UPLOAD_FAILED = "The upload was unable to complete successfully."
ERROR_DOCUMENT_DOES_NOT_EXIST = "Document '%s' does not exist."
ERROR_INVALID_THRESHOLD = "Threshold must be 'verylow', 'low', 'medium', 'high' or 'veryhigh'."
ERROR_QUESTION_DOES_NOT_EXIST = "A question with the ID '%s' does not exist."
ERROR_ANSWER_DOES_NOT_EXIST = "An answer with the ID '%s' does not exist."
CANNOT_BE_POST_PARAM = "Parameter '%s' is special and can only be a GET parameter, i.e. in the url."
CANNOT_BE_GET_PARAM = "Parameter '%s' is special and can only be a POST parameter."
ERROR_INVALID_JSON = "Could not read the request, if using JSON please check the format, i.e. use \"double-quotes\" and not 'single-quotes'."
ERROR_INVALID_SOURCE_TYPE = "Invalid sourceType, must be either 'document', 'saved_reply' or 'all'."
ERROR_INVALID_SPEED_OR_ACCURACY = "Invalid speedOrAccuracy, must be either 'speed', 'balanced' or 'accuracy' but got %s."
ERROR_INVALID_TERMS = "Invalid termsAgreed, must be either 'true' or 'false' but got %s."
ERROR_INVALID_USAGE = "Invalid usage of API, for example requests containing invalid utf-8 characters."
ERROR_USER_DOES_NOT_EXIST = "User '%s' does not exist."
# Saved Replies
ERROR_REPLY_DOES_NOT_EXIST = "Saved reply '%s' does not exist."
ERROR_REPLY_ALREADY_EXISTS = "A reply for the question '%s' already exists."
ERROR_NO_SAVED_REPLY_STORE = "Could not find any saved reply."
ERROR_INVALID_SLACK_RESPONSE = "Invalid response from Slack."
ERROR_SLACKBOT_ALREADY_EXISTS = "Slackbot '%s' already exists."
ERROR_ANNOTATION_DOES_NOT_EXIST = "Annotation '%s' does not exist."
ERROR_ANNOTATION_LAST_ANSWER = "At least one answer must be associated with an annotation."
ERROR_ANNOTATION_MISSING_PARAMS = "Both the 'startOffset' and 'endOffset' parameters must be set."
ERROR_ANNOTATION_ALREADY_EXISTS = "An annotation for the question '%s' already exists for this document."
ERROR_INVALID_BOUNDING_BOX = "Bounding boxes must contain a '%s' key."
ERROR_UNRECOGNISED_SENDER = "Sorry, your email address (%s) does not have permission to modify saved replies."
ERROR_EMAIL_UNCONFIGURED = "Sorry, this Cape AI account has not yet been configured for email access.<br /><br />" \
                           "Please contact your Cape administrator to set this up."
ERROR_INVALID_EMAIL = "Invalid email address '%s'"
ERROR_EMAIL_TOKEN_NOT_FOUND = "Sorry, a user with the token '%s' could not be found.<br /><br />" \
                              "Please contact your Cape administrator for the correct token."
ERROR_NO_SUGGESTIONS = "Unfortunately Cape was unable to find any suggestions for this question."

# Remote debugging
DEBUG_SERVER_CONNECTION_FAILURE = "Connection failure to debug server"

# PDF Service
ERROR_FAILED_TO_PROCESS_PDF = "Failed to process pdf, please retry later."

# Email
MAILGUN_INVALID_SIGNATURE = "Invalid credential supplied"
ERROR_INVALID_EMAIL_TOKEN = "Invalid verification token supplied %s, make sure you are logged-in with the user that provided the email where this token was found."
ERROR_EMAIL_UNVALIDATED ="Sorry, this Cape AI account has an email that has not been verified.<br /><br />" \
                         "Please contact your Cape administrator to set this up."

# Bots
ERROR_FILE_TYPE_UNSUPPORTED = "Sorry, I can only understand plain text and markdown files at the moment."
BOT_FILE_UPLOADED = "Thanks! I'll use that to help me answer your questions."
