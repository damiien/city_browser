from flask import json, Response

def create_response(res, status_code):

  return Response(
    mimetype="application/json",
    response=json.dumps(res),
    status=status_code
  )
