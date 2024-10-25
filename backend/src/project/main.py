from project.adapters.AnswerRouter import AnswerRouter
from project.adapters.Settings import Settings
from project.adapters.OpenAILLM import OpenAILLM
from project.adapters.VectorDatabaseEnricher import VectorDatabaseEnricher
from project.core.ChatService import ChatService
from project.adapters.AnswerTemplate import AnswerTemplate

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager


def _inject_routers(api: FastAPI, router: AnswerRouter):
    api.include_router(router.create())


@asynccontextmanager
async def _setup(api: FastAPI, settings: Settings):
    context_enricher = VectorDatabaseEnricher()
    llm_answerer = OpenAILLM()
    template = AnswerTemplate()
    service = ChatService(context_enricher, llm_answerer, template, settings)
    router = AnswerRouter(service)
    _inject_routers(api, router)
    yield


def _create_api(settings: Settings):
    project_api = FastAPI(
        title="D&D answerer API",
        version="0.1",
        lifespan=lambda api: _setup(api, settings),
    )

    project_api.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_origins=settings.api.allowed_origins,
        allow_methods=settings.api.allowed_methods,
        allow_headers=settings.api.allowed_headers,
    )

    return project_api


def _run_uvicorn(settings: Settings):
    uvicorn.run(
        app="project.main:project_api",
        host=str(settings.api.host),
        port=settings.api.port,
    )


project_settings = Settings.load()
project_api = _create_api(project_settings)

if __name__ == "__main__":
    _run_uvicorn(project_settings)
