function xAjax(method, url, async, hookFun) {
	this.xmlHttp = window.ActiveXObject ? new ActiveXObject("Microsoft.XMLHTTP") : new XMLHttpRequest();
	
    if (this.xmlHttp != null) {
        if (hookFun)
        {
            this.xmlHttp.onreadystatechange = hookFun;
        }
		this.xmlHttp.open(method, url, async);
		if (method == "POST") {
			this.xmlHttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
		}
	}
	
	this.send = function(content) {
		this.xmlHttp.send(content);
	}	
}

function xJSon() {
	var json = {};
	
	this.addItem = function(prop, val) {
		json[prop] = val;
	}
	
	this.delItem = function(prop) {
		delete json[prop];
	}
	
	this.modify = function(prop, newVal) {
		json[prop] = newVal;
	}
	
	this.getItem = function(prop) {
		return json[prop];
	}
}

function loadXML(xmlUrl)
{
	var xmlDoc = null;
	
	if(!window.DOMParser && window.ActiveXObject)
	{
		var xmlDomVersions = ['MSXML.2.DOMDocument.6.0','MSXML.2.DOMDocument.3.0','Microsoft.XMLDOM'];
		var len = xmlDomVersions.length;
		
		for(var i=0; i<len; i++)
		{
			try{
				xmlDoc = new ActiveXObject(xmlDomVersions[i]);
				xmlDoc.async = false;
				xmlDoc.loadXML(xmlUrl);
				break;
			}catch(e){}
		}
	}
	else if(window.DOMParser && document.implementation && document.implementation.createDocument)
	{
		try{
			domParser = new DOMParser();
			xmlDoc = domParser.parseFromString(xmlUrl, 'text/xml');
		}catch(e){}
	}
	return xmlDoc;
}

function setXML2Array(xmlDoc, parentNode, subnodeArray, BWspecial){
	var nodes = xmlDoc.documentElement.getElementsByTagName(parentNode);
	var nodeLen = nodes.length;
	var arrayLen = subnodeArray.length;
	var resArray = new Array();

	for(var i=0; i<nodeLen; i++){
		resArray[i] = new Array();
		var fullName = "";
		for(var j=0; j<arrayLen; j++){
			if(BWspecial == "true"){
				if(j == 0){
                    fullName = getNodeValue(nodes[i], subnodeArray[j]);
				}else if(j ==1){
                    resArray[i][0] = fullName + getNodeValue(nodes[i], subnodeArray[j]);
				}else{
                    resArray[i][j - 1] = getNodeValue(nodes[i], subnodeArray[j]);
				}
			}else{
                resArray[i][j] = getNodeValue(nodes[i], subnodeArray[j]);
			}
		}
	}

	return resArray;
}


function getNodeValue(node, name){
	var subNodes = node.getElementsByTagName(name);
	if(subNodes != null && subNodes.length != 0){
        return subNodes[0].firstChild == null ? "" : subNodes[0].firstChild.nodeValue;
	}else{
		var blank = "";
		return blank;
	}
}
