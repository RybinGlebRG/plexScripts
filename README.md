# plexScripts

This project was created as a solution to Plex Media Server strict naming convention problem.
PMS requires to name your files in a very specific way.  But files can originally contain a lot of info in their names: resolution, language, year, etc.
Just erasing all that data is not an option. Idea was to create symlinks for files with proper names. Note that creating symlinx works in *nix systems.
Obviously, the best solution is to write a Scanner for Plex, but it requires a lot of studying of Plex source code. 
More so these scripts can be used as a basis to Plex Scanner.
So, aren't Python scripts that analyze data and create symlinks make for most optimal solution? I think so. 

