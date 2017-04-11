var current=1;
setback(current);

function left_button(){
	current=dec(current);
	setback(current);
}
function right_button(){
	current=inc(current);
	setback(current);
}

function dec(curr){
	if(curr==1)
		curr=4;
	else
		curr--;
	return curr;
}

function inc(curr){
	if(curr==4)
		curr=1;
	else
		curr++;
	return curr;
}

function setback(index){
	document.getElementById("diwalidiv").style.backgroundImage="url(static/"+index.toString()+".jpg)";
}
