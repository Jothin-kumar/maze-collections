set -e

if [ -d "build" ]
then
    cd build
    git pull
    cd ../
else
    git clone https://github.com/Jothin-kumar/build.git
fi
printf "git (build) ✅\n\n"

python3 py/repair-maze.py
printf "repair-maze.py ✅\n\n"

python3 py/make.py
printf "make.py ✅\n\n"

python3 build/build.py
printf "build.py ✅\n\n"

cp -r maze build-output/maze
printf "maze data ✅\n\n"

cp stats.txt build-output/stats.txt
printf "stats.txt ✅\n\n"

cp root/_redirects build-output/_redirects
printf "_redirects ✅\n\n"

cp root/robots.txt build-output/robots.txt
printf "robots.txt ✅\n\n"