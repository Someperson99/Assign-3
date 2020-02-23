# Assign-3
This will create tuples(word, object) each object contains{docId,count} in each iteration, after the iteration ends it will then save the tuples into a list of tuples. most likely there going to be dublicates of the same word in the disk but each with diffrent object as their related docId and their count, i could add positions too but it is an extra iteration just for the position if it is nessasary. it will be easy to sort the list at the end of maybe the 10 iteration as we agreed on, probebly need to add counter and than sort then at the end before we write it to the disk. 

so it will show in the disk : 
uci docId 0 count 6
uci docId 1 count 2

which is fine i believe.

i have a problem with the implemantion of the way i am getting the json file, i am not able to get url of it, to be able to save it into the dictionary that it is supposed to keep track of the (docId --> url) so if i can not get the first url i might have to change the way get_all_json() function works.
