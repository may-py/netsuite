define(['N/format', 'N/search', 'N/format', 'N/file'], function (format, search, format, file) {
    function _get(context) {
        try {
            var data = getDataFormSS();
            if (typeof (data) === 'object') {
                return {
                    code: 200,
                    status: 'success',
                    data: data,
                };
            }
            else {
                return {
                    code: 500,
                    status: 'error',
                    error: data
                };
            }

        } catch (err) {
            return {
                code: 500,
                error: err
            };
        }
    }
    function getDataFormSS() {
        var arrData = [];
        var rs = search.load(
            {
                id: xxxx  //<<<<<<<<<<<<<<<<<<<  UPDATE internal Id 
            });
        var cols = rs.columns;
        var result = getAllResults(rs);
        for (var i = 0; i < result.length; i++) {
            var key1 = result[i].getValue(cols[0]); //key can rename anything you want 
            var key2 = result[i].getValue(cols[1]);
            var key3 = result[i].getValue(cols[2]);
            var key4 = result[i].getValue(cols[3]);
            var key5 = result[i].getValue(cols[4]);
            var key6 = result[i].getValue(cols[5]);
            var key7 = result[i].getValue(cols[6]);
            var key8 = result[i].getValue(cols[7]);
            var key9 = result[i].getValue(cols[8]);
            var key10 = result[i].getValue(cols[9]);
            var key11 = result[i].getValue(cols[10]);
            var key12 = result[i].getValue(cols[11]);
            var key13 = result[i].getValue(cols[12]);
            var key14 = result[i].getValue(cols[13]);
            var key15 = result[i].getValue(cols[14]);
            var key16 = result[i].getValue(cols[15]);
            var key17 = result[i].getValue(cols[16]);
            var key18 = result[i].getValue(cols[17]);
            var key19 = result[i].getValue(cols[18]);
            var key20 = result[i].getValue(cols[19]);
            var key21 = result[i].getValue(cols[20]);
          	var key22 = result[i].getValue(cols[21]);
          	var key23 = result[i].getValue(cols[22]);
          	var key24 = result[i].getValue(cols[23]);

            arrData.push({
              key1:key1,key2:key2,key3:key3,key4:key4,key5:key5,key6:key6,key7:key7,key8:key8,key9:key9,
              key10:key10,key11:key11,key12:key12,key13:key13,key14:key14,key15:key15,key16:key16,key17:key17,key18:key18,
              key19:key19,key20:key20,key21:key21,key22:key22,key23:key23,key24:key24,


            });
        }
        return arrData;
    }
    function getAllResults(s) {
        var results = s.run();
        var searchResults = [];
        var searchId = 0;
        do {
            var resultSlice = results.getRange({ start: searchId, end: searchId + 1000 });
            resultSlice.forEach(function (slice) {
                searchResults.push(slice);
                searchId++;
            });

        } while (resultSlice.length >= 1000);
        return searchResults;
    }
    return {
        get: _get,
        // post: _post,

    }
});
