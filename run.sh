#!/bin/sh
# run.sh
# 2023-01-05 | CR
#
APP_DIR='src'
ENV_FILESPEC=""
if [ -f "./.env" ]; then
    ENV_FILESPEC="./.env"
fi
if [ -f "../.env" ]; then
    ENV_FILESPEC="../.env"
fi
if [ "$ENV_FILESPEC" != "" ]; then
    set -o allexport; source ${ENV_FILESPEC}; set +o allexport ;
fi
if [ "$1" = "deactivate" ]; then
    cd ${APP_DIR} ;
    deactivate ;
fi
if [[ "$1" != "deactivate" && "$1" != "pipfile" && "$1" != "clean" && "$1" != "test" ]]; then
    python3 -m venv ${APP_DIR} ;
    . ${APP_DIR}/bin/activate ;
    cd ${APP_DIR} ;
    if [ -f "requirements.txt" ]; then
        pip3 install -r requirements.txt
    else
        pip install beautifulsoup4
        pip install requests
        pip install fastapi
        pip install a2wsgi
        pip freeze > requirements.txt
    fi
fi
if [ "$1" = "pipfile" ]; then
    deactivate ;
    pipenv lock
fi
if [ "$1" = "clean" ]; then
    echo "Cleaning..."
    deactivate ;
    rm -rf __pycache__ ;
    rm -rf bin ;
    rm -rf include ;
    rm -rf lib ;
    rm -rf pyvenv.cfg ;
    rm -rf ../.vercel/cache ;
    ls -lah
fi

if [[ "$1" = "run_module" || "$1" = "" ]]; then
    echo "Run module only..."
    echo "pwd: $(pwd)"
    echo ""
    python -m index cli
    echo ""
    echo "Done..."
fi

if [ "$1" = "run" ]; then
    echo "Run..."
    cd ..
    vercel dev --listen 0.0.0.0:5001 ;
    echo "Done..."
fi
if [ "$1" = "deploy_prod" ]; then
    cd ..
    vercel --prod ;
fi
if [ "$1" = "rename_staging" ]; then
    cd ..
    vercel alias $2 ${APP_NAME}-staging-tomkat-cr.vercel.app
fi
