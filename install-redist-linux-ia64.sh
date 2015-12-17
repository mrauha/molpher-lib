$PREFIX=~/Molpher/

function build_deps()
{
    echo "Molpher Install: Building boost..."
    cd $PREFIX/dependencies/
    ./build-deps-linux-backend-ia64.sh --boost
    echo "Molpher Install: Building rdkit..."
    ./build-deps-linux-backend-ia64.sh --rdkit
    echo "Molpher Install: Building zlib..."
    ./build-deps-linux-backend-ia64.sh --zlib
    echo "Molpher Install: Building rcf..."
    ./build-deps-linux-backend-ia64.sh --rcf
    echo "Molpher Install: Building tbb..."
    ./build-deps-linux-backend-ia64.sh --tbb
}

function build_molpher()
{
    echo "Molpher Install: Building Molpher..."
    cd $PREFIX/backend/
    make CONF=Linux64_Debug_library
}

function build_molpher_lib()
{
    echo "Molpher Install: Building Molpher-lib..."
    cd $PREFIX/molpher-lib/
    make CONF=Linux64_Debug
}

# prepare directories
$PREFIX=$(realpath $PREFIX)
mkdir -f $PREFIX
cp -r . $PREFIX

if build_deps() && build_molpher() && build_molpher_lib(); then
    echo "Molpher-lib was built successfully!"
fi