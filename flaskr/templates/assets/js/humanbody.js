/*window.onload = function () {
    const front_pieces = document.getElementsByClassName('human-front');
        console.log(front_pieces.length);

    for (var i = 0; i < front_pieces.length; i++) {
        let back_piece = front_pieces[i];
        
        back_piece.onclick = function(t) {
            if (t.target.getAttribute('data-position') != null) document.getElementById('data').innerHTML = t.target.getAttribute('data-position');
            if (t.target.parentElement.getAttribute('data-position') != null) document.getElementById('data').innerHTML = t.target.parentElement.getAttribute('data-position');
        }
    }
    
    const back_pieces = document.getElementsByClassName('human-back');
        console.log(back_pieces.length);

    for (var i = 0; i < back_pieces.length; i++) {
        let back_piece = back_pieces[i];
        
        back_piece.onclick = function(t) {
            if (t.target.getAttribute('data-position') != null) document.getElementById('data').innerHTML = t.target.getAttribute('data-position');
            if (t.target.parentElement.getAttribute('data-position') != null) document.getElementById('data').innerHTML = t.target.parentElement.getAttribute('data-position');
        }
    }
}*/
const treatment = {
    "head": "Head<br> <ul><li>Applying a cold pack to the area can help to reduce swelling.</li><li>Take Tylenol but should avoid non-steroidal anti-inflammatory drugs (NSAIDs), such as ibuprofen and aspirin, unless a doctor prescribes them.</li><br>Prevention: Wear seatbelt. Wear helmet. Follow safety precautions.</ul>",
    "shoulder-right": "Shoulder <br><ul><li>Use good posture when you sit or stand.</li> <li>Follow the rules for safe lifting.</li><li>Keep your back straight and use your legs.</li><li>Take a break for a couple of minutes every hour. </li><li>Move around and stretch.If you work at a desk, make sure your work station is set up so that you can comfortably use your computer.</li><a href=\"Shoulder.html\">More</a></ul>",
    "shoulder-left": "Shoulder <br><ul><li>Use good posture when you sit or stand.</li> <li>Follow the rules for safe lifting.</li><li>Keep your back straight and use your legs.</li><li>Take a break for a couple of minutes every hour. </li><li>Move around and stretch.If you work at a desk, make sure your work station is set up so that you can comfortably use your computer.</li><a href=\"Shoulder.html\">More</a></ul>",
    "upper-arm-right": "",
    "upper-arm-left": "",
    "lower-arm-right": "",
    "lower-arm-left": "",
    "elbow-right": "",
    "elbow-left": "",
    "chest": "",
    "stomach": "",
    "hand-right-wrist": "Wrist<br> <ul>Immediate treatment for an injured wrist should involve the following steps<li>Immobilize the wrist using a splint or brace.</li><li>Elevate the wrist above the level of the heart.</li><li>Use ice therapy on the injured area for 10 to 15 minutes every hour. Regular icing can significantly ease swelling and pain.</li><br>If the injury is a wrist sprain, the pain and swelling should begin to subside within 48 hours. If significant pain persists after a few days of treatment, it’s important to see a physician for an exam and x-ray. Some types of wrist fractures can cause mild or vague symptoms and be difficult to detect, but they need treatment.</ul>",
    "hand-left-wrist": "Wrist<br> <ul>Immediate treatment for an injured wrist should involve the following steps<li>Immobilize the wrist using a splint or brace.</li><li>Elevate the wrist above the level of the heart.</li><li>Use ice therapy on the injured area for 10 to 15 minutes every hour. Regular icing can significantly ease swelling and pain.</li><br>If the injury is a wrist sprain, the pain and swelling should begin to subside within 48 hours. If significant pain persists after a few days of treatment, it’s important to see a physician for an exam and x-ray. Some types of wrist fractures can cause mild or vague symptoms and be difficult to detect, but they need treatment.</ul>",
    "upper-leg-right": "Leg<br>Treatment for a leg injury may include rest, ice, elevation, and other first aid measures (such as the application of a brace, splint, or cast)<br><a href=\"Leg.html\">More</a><br>",
    "upper-leg-left": "Leg<br>Treatment for a leg injury may include rest, ice, elevation, and other first aid measures (such as the application of a brace, splint, or cast)<br><a href=\"Leg.html\">More</a><br>",
    "lower-leg-right": "Leg<br>Treatment for a leg injury may include rest, ice, elevation, and other first aid measures (such as the application of a brace, splint, or cast)<br><a href=\"Leg.html\">More</a><br>",
    "lower-leg-left": "Leg<br>Treatment for a leg injury may include rest, ice, elevation, and other first aid measures (such as the application of a brace, splint, or cast)<br><a href=\"Leg.html\">More</a><br>",
    "knee-right": "Leg<br>Treatment for a leg injury may include rest, ice, elevation, and other first aid measures (such as the application of a brace, splint, or cast)<br><a href=\"knee.html\">More</a><br>",
    "knee-left": "Leg<br>Treatment for a leg injury may include rest, ice, elevation, and other first aid measures (such as the application of a brace, splint, or cast)<br><a href=\"knee.html\">More</a><br>",
    "ankle-right": "Ankle<br>For self-care of an ankle sprain, use the R.I.C.E. approach for the first two or three days:<br>Rest. Avoid activities that cause pain, swelling or discomfort.<br>Ice. Use an ice pack or ice slush bath immediately for 15 to 20 minutes and repeat every two to three hours while you're awake. If you have vascular disease, diabetes or decreased sensation, talk with your doctor before applying ice.<br>Compression. To help stop swelling, compress the ankle with an elastic bandage until the swelling stops. Don't hinder circulation by wrapping too tightly. Begin wrapping at the end farthest from your heart.<br>Elevation. To reduce swelling, elevate your ankle above the level of your heart, especially at night. Gravity helps reduce swelling by draining excess fluid.<br><a href=\"Ankle.html\">More</a><br>",
    "ankle-left": "Ankle<br>For self-care of an ankle sprain, use the R.I.C.E. approach for the first two or three days:<br>Rest. Avoid activities that cause pain, swelling or discomfort.<br>Ice. Use an ice pack or ice slush bath immediately for 15 to 20 minutes and repeat every two to three hours while you're awake. If you have vascular disease, diabetes or decreased sensation, talk with your doctor before applying ice.<br>Compression. To help stop swelling, compress the ankle with an elastic bandage until the swelling stops. Don't hinder circulation by wrapping too tightly. Begin wrapping at the end farthest from your heart.<br>Elevation. To reduce swelling, elevate your ankle above the level of your heart, especially at night. Gravity helps reduce swelling by draining excess fluid.<br><a href=\"Ankle.html\">More</a><br>",
    "foot-right": "",
    "foot-left": ""
};

window.onload = function() {
    const front_pieces = document.getElementsByClassName('human-front');
    var flag = 0;
    var arr = new Array();
    for (var i = 0; i < front_pieces.length; i++) {
        let back_piece = front_pieces[i];
        back_piece.onclick = function(t) {
            if (flag === 0) {
                document.getElementById('data').innerHTML = "";
                document.getElementById('recommendation').innerHTML = "";
                flag++;
            }
            //Body part selected
            if (t.target.getAttribute('data-position') != null) {
                //To delete already selected
                if (arr.includes(t.target.getAttribute('data-position'))) {
                    for (var i = 0; i < arr.length; i++) {
                        if (arr[i] === t.target.getAttribute('data-position')) {
                            arr.splice(i, 1);
                            i--; // Since the indexes of elements following this index get updated after removal
                        }
                    }
                    //Duplicate click to remove body parts
                    document.getElementById('data').innerHTML = "";
                    document.getElementById('recommendation').innerHTML = "";

                    for (var i = 0; i < arr.length; i++) {
                        document.getElementById('data').innerHTML += arr[i] + " ";
                        document.getElementById('recommendation').innerHTML += treatment[arr[i]];
                        console.log(arr[i]);

                    }
                    if (arr.length === 0) {
                        document.getElementById('data').innerHTML = "None";
                        document.getElementById('recommendation').innerHTML = "None";
                        flag = 0;
                    }

                    document.getElementsByClassName(t.target.getAttribute('data-position'))[0].style.fill = '#57c9d5';

                } else {
                    document.getElementById('data').innerHTML += t.target.getAttribute('data-position') + " ";
                    arr.push(t.target.getAttribute('data-position'));
                    var part = t.target.getAttribute('data-position');
                    document.getElementById('recommendation').innerHTML += treatment[part];
                    document.getElementsByClassName(t.target.getAttribute('data-position'))[0].style.fill = '#ff7d16';
                }
            }
        }

    }

    const back_pieces = document.getElementsByClassName('human-back');
    console.log(back_pieces.length);

    for (var i = 0; i < back_pieces.length; i++) {
        let back_piece = back_pieces[i];

        back_piece.onclick = function(t) {
            //if (t.target.getAttribute('data-position') != null) document.getElementById('data').innerHTML = t.target.getAttribute('data-position');
            if (flag === 0) {
                document.getElementById('data').innerHTML = "";
                flag++;
            }
            //Body part selected
            if (t.target.getAttribute('data-position') != null) {
                //Check duplicate and remove
                if (arr.includes(t.target.getAttribute('data-position'))) {
                    for (let i = 0; i < arr.length; i++) {
                        if (arr[i] === t.target.getAttribute('data-position')) {
                            arr.splice(i, 1);
                            i--;
                        }
                    }
                    //Duplicate click to remove body parts
                    document.getElementById('data').innerHTML = "";
                    for (let i = 0; i < arr.length; i++) {
                        document.getElementById('data').innerHTML += arr[i] + " ";
                    }
                    //When non selected
                    if (arr.length === 0) {
                        document.getElementById('data').innerHTML = "None";
                        flag = 0;
                    }
                    document.getElementsByClassName(t.target.getAttribute('data-position'))[0].style.fill = '#57c9d5';

                } else {
                    document.getElementById('data').innerHTML += t.target.getAttribute('data-position') + " ";
                    arr.push(t.target.getAttribute('data-position'));
                    document.getElementsByClassName(t.target.getAttribute('data-position'))[0].style.fill = '#ff7d16';
                }
            }
        }
    }

}
$('#button').click(function() {
    $("#colormethis").toggleClass('active');
});