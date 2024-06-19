PATH= /mnt/c/Users/Dell/Desktop/AnalysisTools/HomeWorks/shell_script_homework/echo.py


echo_data=("element1", "table2", "array3", "point4")



for i in {0..3}
do
    /usr/bin/python3 echo.py $i ${echo_data[i]}
done

