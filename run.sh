#!/bin/sh
# run.sh
# 2023-01-05 | CR
#

run_clean() {
    cd ${APP_DIR} ;
    echo "Cleaning..."
    # deactivate ;
    rm -rf __pycache__ ;
    rm -rf bin ;
    rm -rf include ;
    rm -rf lib ;
    rm -rf pyvenv.cfg ;
    rm -rf ../.vercel/cache ;
    ls -lah
    cd ..
}

run_venv() {
    python3 -m venv ${APP_DIR} ;
    . ${APP_DIR}/bin/activate ;
    cd ${APP_DIR} ;
    if [ -f "requirements.txt" ]; then
        pip3 install -r requirements.txt
    else
        pip install --upgrade pip

        # poetry add setuptools beautifulsoup4 requests
        pip install \
            beautifulsoup4 \
            requests

        pip install \
            fastapi \
            a2wsgi

        pip freeze > requirements.txt
    fi
}

APP_DIR='bcv_exchange_rates'
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

if [ "$1" = "pipfile" ]; then
    deactivate ;
    pipenv lock
fi

if [ "$1" = "clean" ]; then
    run_clean
fi

if [ "$1" = "update" ]; then
    run_clean
    rm -rf ${APP_DIR}/requirements.txt
    run_venv
fi

if [[ "$1" = "run_module" || "$1" = "run" || "$1" = "" ]]; then
    run_venv
    cd ..
    echo "Run module only..."
    echo "pwd: $(pwd)"
    echo ""
    echo "BCV Exchange Rates"
    echo ""
    if jq --version > /dev/null 2>&1; then
        python -m bcv_exchange_rates.index cli | jq .
    else
        python -m bcv_exchange_rates.index cli
    fi
    echo ""
    echo "Done..."
fi

if [ "$1" = "run_vercel" ]; then
    run_venv
    echo "Run..."
    cd ..
    vercel dev --listen 0.0.0.0:5001 ;
    echo "Done..."
fi

if [ "$1" = "deploy_prod" ]; then
    run_venv
    cd ..
    vercel --prod ;
fi

if [ "$1" = "rename_staging" ]; then
    run_venv
    cd ..
    vercel alias $2 ${APP_NAME}-staging-tomkat-cr.vercel.app
fi
