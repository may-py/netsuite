// Go to the debug place inside Netsuite. 

require(['N/record'], function(record){
  var ret = []
  var objRecord = record.load({
      type: record.Type.INVOICE,  //Change the record.type.xxxxx that you might looking for debug
      id: xxxx,   // Update one record id.
      isDynamic: true,
  });
  
  ret.push('obj',objRecord )
  log.debug(ret)
  return ret;
   
  var x =0;
})
