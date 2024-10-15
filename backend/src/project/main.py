from project.adapters.OpenAILLM import OpenAILLM
from project.adapters.VectorDatabaseEnricher import VectorDatabaseEnricher
from project.adapters.AnswerRouter import AnswerRouter
from project.adapters.Settings import Settings

from project.core.ChatService import ChatService

# import aiohttp
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def _inject_routers(api: FastAPI):
    api.include_router(AnswerRouter.create())


async def _setup(api: FastAPI):
    _inject_routers(api)


def _create_api(settings: Settings):
    project_api = FastAPI(
        title="D&D answerer API",
        version="0.1",
        lifespan=lambda api: _setup(api),
    )

    project_api.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allowed_origins=settings.api.allowed_origins,
        allowed_methods=settings.api.allowed_methods,
        allowed_headers=settings.api.allowed_headers,
    )

    return project_api


def _run_uvicorn(settings: Settings):
    uvicorn.run(
        app="project.main:project_api",
        host=str(settings.api.host),
        port=settings.api.port,
    )


# def create_answer(query):
#    context_enricher = VectorDatabaseEnricher()
#    llm_answerer = OpenAILLM()
#    settings = SecurityVariables()
#    service = ChatService(context_enricher, llm_answerer, settings)
#    router = AnswerRouter(service)

project_settings = Settings.load()
project_api = _create_api(project_settings)

if __name__ == "__main__":
    _run_uvicorn(project_settings)
