from flask import Flask, jsonify
from flask_restful import Resource, Api
from apispec import APISpec
from marshmallow import Schema, fields
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec
from flask_apispec.views import MethodResource
from flask_apispec import marshal_with, doc, use_kwargs

def getController():
    class exampleController(MethodResource, Resource):
        class AwesomeResponseSchema(Schema):
            message = fields.Str(default='Success')

        class AwesomeRequestSchema(Schema):
            api_type = fields.String(required=True, description="API type of awesome API")
    
        @doc(description='My First GET Awesome API.', tags=['Awesome'])
        @marshal_with(AwesomeResponseSchema)  # marshalling
        def get(self):
            '''
            Get method represents a GET API method
            '''
            return {'message': 'My First Awesome API'}

        @doc(description='My First GET Awesome API.', tags=['Awesome'])
        @use_kwargs(AwesomeRequestSchema, location=('json'))
        @marshal_with(AwesomeResponseSchema)  # marshalling
        def post(self):
            '''
            Post method represents a POST API method
            '''
            return {'message': 'My First Awesome API'}
    return exampleController