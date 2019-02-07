import pytest
from . import sample_lib

def pretty(string):
    import pprint
    pp = pprint.PrettyPrinter(indent=4)
    return pp.pprint(string)

def test_authenticate_mfa_session_token():
    cxn = {
        'DurationSeconds': 3600,
        'SerialNumber': 'arn:aws:iam::644138682826:mfa/garet-wright',
        'TokenCode': '12345'
    }
    session_token = sample_lib.authenticate_mfa_session_token(**cxn)
    pretty(session_token)

def test_generate_authorized_session():


def test_new_session_resource():
    res = 'ec2'
    session = sample_lib.new_session_resource(session, res)

def test_get_ami_data():
    ami = 'ami-0cc7ef262a06d2551'





































# ########################################################
# ## This Function will fail
# ## We know it will fail. What do we do? We may still want it in our tests!
# ########################################################
# ## @wtf.are.these(?) - they're called "decorators"
# ## they inform pytest that we want to wrap this function in another function
# ## it's invisible to us, but we've marked the following function to `xfail` or
# ## "expected failure" because in this case, Line 16 is incorrect syntax.
# @pytest.mark.xfail(reason="""
#     Example Failure; Headers is incorrect.
# """)
# def test_get_url_explicit_args_failure():
#     r = sample_lib.get_url_explicit_args(
#         url = "https://google.com",
#         headers = {
#             'Content-Type: application/json'
#         }
#     )
#     assert(r.status_code == 200)

# #########################################################
# ## These will succeed
# #########################################################
# def test_get_url_explicit_args():
#     r = sample_lib.get_url_explicit_args(
#         url = "https://google.com",
#         headers = {
#             'Content-Type': 'application/json'
#         }
#     )
#     assert r.status_code == 200

# def test_get_url_keyword_args():
#     arguments = {
#         "url": "http://www.json.org/example.html?",
#         "headers": {
#             'Content-Type': 'application/json'
#         }
#     }
#     r = sample_lib.get_url_kwargs(**arguments)
#     assert r.status_code == 200

# ############################################################
# ## This one will be skipped
# ############################################################
# ## Down here, we can "decorate" our test with a `skip()` function
# ## We may not know what this function does, exactly, but we know we'll
# ## need it at some point in the future, so why not write something around it?
# @pytest.mark.skip(reason="It should do some future thing")
# def test_some_future_function():
#     what_it_does = "i don't really know yet, but that's okay"
#     vague_idea = 1
#     assert vague_idea == 1
