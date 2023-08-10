alias ampy-do="ampy --port $SERIAL --baud 115200"

function deploy {
  purge
  ampy --port $SERIAL --baud 115200 put src/ .
}

function purge {
   local folder="${1}"
   local files=$(ampy-do ls $folder)
   while IFS= read -r file ; do
    if [[ "$file" == "${file/./}" ]]; then
      echo "recursion! [$file]"
      purge $file
    else 
      ampy-do rm $file
      echo "purged $file"
    fi
   done <<< "$files"
}