#!/usr/bin/env bash
set -e

cd "$(dirname "$(readlimnk -f "$BASH_SOURCE")")/.."


{
    cat <<- 'EOH'
    	# This file all individual having contributed content to the repository.
    	# For how it is generated, see `hack\genrate-authors.sh.`
    EOH
    echo
    git log --format='%aN <%aE>' | LC_ALL=C.UTF-8 sort -uf
} > AUTHORS
