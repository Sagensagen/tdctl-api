import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import config

from .api import members, auth, events, admin, mail, jobs
from .db import setup_db


def create_app():

    app = FastAPI(
        title='TDCTL-API',
        version="0.1",
        description='''TDCTL-database API. 
        Everything related to Tromsøstudentenes Dataforening''',
        contact={'name': 'td', 'email': 'td@list.uit.no'},
        docs_url="/",
    )

    # CORS Middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=['http://localhost:3000', 'https://td-uit.no', 'k8s.td.org.uit.no'],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Routers
    app.include_router(members.router, prefix="/api/member", tags=['members'])
    app.include_router(auth.router, prefix="/api/auth", tags=['auth'])
    app.include_router(events.router, prefix="/api/event", tags=['event'])
    app.include_router(admin.router, prefix="/api/admin", tags=['admin'])
    app.include_router(mail.router, prefix="/api/mail", tags=['mail'])
    app.include_router(jobs.router, prefix="/api/jobs", tags=['job'])

    # Fetch config object
    env = os.getenv('API_ENV', 'default')
    app.config = config[env]

    setup_db(app)
    # Set tokens to expire at at "exp"
    app.db.tokens.create_index("exp", expireAfterSeconds=0)

    return app
