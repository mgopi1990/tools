
## snippet used to rename scanned files to names with proper prefix
## modify the below parameters 
src=6
dest=1
src_prefix="scan"
dest_prefix="aricent4_cw"
n=`ls | wc -l`
echo "# total files: $n"

## reports any missing files
report_missing_source_file() {
 ret_val=0
 temp_src=$src
 for i in `seq 1 ${n}`
 do
  temp_file=`printf "${src_prefix}%04d.jpg" $temp_src`
  if [ ! -e $temp_file ]
  then
   echo "# ERROR: missing $temp_file"
   ret_val=1
  fi
 temp_src=`expr $temp_src + 1`
 done

 return $ret_val
}

## generates mv command to rename
generate_rename() {
 report_missing_source_file
 if [ $? -eq 1 ]
 then
  return 1
 fi

 temp_src=$src
 temp_dest=$dest
 for i in `seq 1 ${n}`;
 do
  printf "mv ${src_prefix}%04d.jpg ${dest_prefix}_%03d.jpg\n" $temp_src $temp_dest
  temp_src=`expr $temp_src + 1`
  temp_dest=`expr $temp_dest + 1`
 done
 
 return 0
}

## invoke it
generate_rename
