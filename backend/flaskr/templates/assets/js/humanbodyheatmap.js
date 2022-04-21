window.onload = function () {
    const front_pieces = document.getElementsByClassName('human-front');
        // console.log(front_pieces.length);

    for (var i = 0; i < front_pieces.length; i++) {
        let back_piece = front_pieces[i];
        
        back_piece.onclick = function(t) {
            console.log(document.getElementById('clickedBodyPartTableTitle').innerHTML);
            if (t.target.getAttribute('data-position') != null)
            {
                var position = t.target.getAttribute('data-position');
                // document.getElementById('data').innerHTML = position;
                document.getElementById('clickedBodyPartTableTitle').innerHTML = position + " " + "Injury Reports";
            } 
            if (t.target.parentElement.getAttribute('data-position') != null)
            {
                var position = t.target.parentElement.getAttribute('data-position');
                // document.getElementById('data').innerHTML = position;
                document.getElementById('clickedBodyPartTableTitle').innerHTML = position + "Injury Reports";
            } 
            
        }
    }
    
    const back_pieces = document.getElementsByClassName('human-back');
        // console.log(back_pieces.length);

    for (var i = 0; i < back_pieces.length; i++) {
        let back_piece = back_pieces[i];
        
        back_piece.onclick = function(t) {
            if (t.target.getAttribute('data-position') != null) document.getElementById('data').innerHTML = t.target.getAttribute('data-position');
            if (t.target.parentElement.getAttribute('data-position') != null) document.getElementById('data').innerHTML = t.target.parentElement.getAttribute('data-position');
            if (t.target.getAttribute('data-position') != null) document.getElementById('clickedBodyPartTableTitle').innerHTML = t.target.getAttribute('data-position');
            if (t.target.parentElement.getAttribute('data-position') != null) document.getElementById('clickedBodyPartTableTitle').innerHTML = t.target.parentElement.getAttribute('data-position');
        }
    }
}