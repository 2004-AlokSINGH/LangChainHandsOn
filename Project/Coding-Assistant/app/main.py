from app.chains.debug_chain import run_debug

log = """
! ssh: connect to host domain.com port 22: Operation timed out
npm ERR! fatal: Could not read from remote repository.
npm ERR!
npm ERR! Please make sure you have the correct access rights
npm ERR! and the repository exists.
npm ERR!
npm ERR! exited with error code: 128
"""

output = run_debug(log)
print(output.model_dump())
