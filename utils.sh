alias ampy-do="ampy --port $SERIAL --baud 115200"

function deploy {
  local refresh="${1}"
  if [ ! -z "$refresh" ]; then
    purge
    echo ""
    echo "----------"
    echo ""
  fi
  echo "Deploying!"
  ampy --port $SERIAL --baud 115200 put management-portal/dist/ www
  ampy --port $SERIAL --baud 115200 put src/ .
  echo "Deploy Done!"
}

function purge {
   local folder="${1}"
   local files=$(ampy-do ls $folder)
   if [ -z $files ] && [ -z $folder ]; then
    echo "Purge Done!"
    return
   fi
   if [ -z $files ] && [ ! -z $folder ]; then
    echo "no files left! purging $folder"
    ampy-do rm $folder
   fi
   while IFS= read -r file ; do
    if [[ "$file" == "${file/./}" ]]; then
      echo "recursion! [$file]"
      purge $file
    else 
      echo "purging $file"
      ampy-do rm $file
    fi
   done <<< "$files"
}
