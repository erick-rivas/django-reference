rm -rf "./bin/sphinx/guides"
rm -rf "./bin/sphinx/index.md"

# Get file list (.md)
array=()
while IFS=  read -r -d $'\0'; do
    array+=("$REPLY")
done < <(find . -name "*.md" -print0)

# Create index.md
touch "./bin/sphinx/index.md"
echo -e "\`\`\`{toctree}" >> "./bin/sphinx/index.md"

# Iterate mds
for i in "${array[@]}"
do
  ignore_sub=$(echo $i| cut -c 3-7)
  bin_sub=$(echo $i| cut -c 3-5)
  md_path=$(echo $i| cut -c 3-)

  if [ $ignore_sub != ".venv" ]; then
    #file=$(echo "$md_path" | tr / -)
    source="./bin/sphinx/guides/$md_path"
    rep_sub=$(echo "$md_path" | sed -e 's/[a-z._A-Z\-]//g' | sed -e 's/[\/]/..\//g' )
    dir=$(dirname "$source")
    content="\`\`\`{include} ../../../$rep_sub$md_path\n\`\`\`"
    mkdir -p $dir
    echo -e "$content" > $source
    if [ $bin_sub != "bin" ]; then
      echo -e "./guides/$md_path" >> "./bin/sphinx/index.md"
    else
      echo -e "{hidden} ./guides/$md_path" >> "./bin/sphinx/index.md"
    fi

  fi
done
echo -e "\`\`\`" >> "./bin/sphinx/index.md"
sphinx-build -E -b html ./bin/sphinx ./bin/sphinx/docs

rm -rf "./bin/sphinx/guides"
rm -rf "./bin/sphinx/index.md"