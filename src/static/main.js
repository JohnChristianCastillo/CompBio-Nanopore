/**
 * Fill in the animal dropdown list
 */
var dir = $(document).ready(function(){
    $.ajax({
        url: `https://CompBio-Nanopore.johnchristianca.repl.co/api/species`,
        //url: `http://127.0.0.1:5000/api/species`,
        type: "GET",
        success: function (data){
            for(var i = 0; i < data["species"].length; ++i){
                $("#chosen_species").append(new Option(data["species"][i], data["species"][i]));
            }
            alphabetizeList("#chosen_species");
        },
        error: function (error){
            console.log(error);
        }
    })

    $.ajax({
        url: `https://CompBio-Nanopore.johnchristianca.repl.co/api/mutatedDNA`,
        //url: `http://127.0.0.1:5000/api/mutatedDNA`,
        type: "GET",
        success: function (data){
            for(var i = 0; i < data["MUTATED_DNA_SEQUENCES"].length; ++i){
                $("#chosen_dna").append(new Option(data["MUTATED_DNA_SEQUENCES"][i], data["MUTATED_DNA_SEQUENCES"][i]));
            }
            alphabetizeList("#chosen_dna");
        },
        error: function (error){
            console.log(error);
        }
    })
})

/**
 * Helper function to alphabetize the dropdown list of train stations
 * @param listField: Field of which we want to alphabetize
 */
function alphabetizeList(listField) {
    var sel = $(listField);
    var selected = sel.val(); // cache selected value, before reordering
    var opts_list = sel.find('option');
    opts_list.sort(function (a, b) {
        return $(a).text() > $(b).text() ? 1 : -1;
    });
    sel.html('').append(opts_list);
    sel.val(selected); // set cached selected value
}

/**
 *  A "Listener" type which helps us detect whether a species has been chosen.
 */
// Clear button click
document.getElementById("chosen_species").addEventListener("change", function(){
    $.ajax({
        url: `https://CompBio-Nanopore.johnchristianca.repl.co/api/sequence/${$('#chosen_species').val()}`,
        //url: `http://127.0.0.1:5000/api/sequence/${$('#chosen_species').val()}`,
        type: "GET",
        success: function (data){
            document.getElementById('scientific_name').innerHTML = data["scientific_name"]
            document.getElementById('sequence').innerHTML = data["sequence"]
            document.getElementById('generated_signal_output').innerHTML = "";
            document.getElementById("generated_mutation_output").innerHTML = "";

        },
        error: function (error){
            console.log(error);
        }
    })
})

/**
 *  A "Listener" type which helps us detect whether the "generate signal" button has been pressed.
 */
document.getElementById("generate_signal").addEventListener("click", function(){
    $.ajax({
        url: `https://CompBio-Nanopore.johnchristianca.repl.co/api/sequence/${$('#chosen_species').val()}`,
        //url: `http://127.0.0.1:5000/api/sequence/${$('#chosen_species').val()}`,
        type: "GET",
        success: function (data){
            $('#generate_signal').fitText
            document.getElementById('generated_signal_output').innerHTML = data["signal"]
        },
        error: function (error){
            console.log(error);
        }
    })
})

/**
 *  A "Listener" type which helps us detect whether the "Find matches" button has been pressed.
 */
// Clear button click
document.getElementById("generate_matches").addEventListener("click", function(){
    $.ajax({
        url: encodeURI(`https://CompBio-Nanopore.johnchristianca.repl.co/api/matcher/species/${$('#chosen_dna').val()}`),
        type: "GET",
        success: function (data){
            $('#generate_signal').fitText
            document.getElementById("matches_info").innerHTML = "Below is a list of data in our database that matches closely with the given DNA sequence\n" +
                "              (listed from the closest match to the furthest match)";
            for(var i = 0; i < data["matches"].length; ++i){
                var match = data["matches"][i];
                var list = document.getElementById("generated_matches_output");
                list.appendChild(document.createElement('li')).appendChild(document.createTextNode(match));
            }
        },
        error: function (error){
            console.log(error);
        }
    })
})

/**
 *  A "Listener" type which helps us detect whether a dna sequence has been chosen.
 */
// Clear button click
document.getElementById("chosen_dna").addEventListener("change", function(){
    document.getElementById("generated_matches_output").innerHTML = "";
})


/**
 *  A "Listener" type which helps us detect whether the "Find matches" button has been pressed.
 */
// Clear button click
document.getElementById("generate_mutation").addEventListener("click", function(){
    var param = $('#generated_signal_output').text();
    $.ajax({
        url: encodeURI(`https://CompBio-Nanopore.johnchristianca.repl.co/api/mutator/`+param),
        type: "GET",
        success: function (data){
            console.log(data);
            document.getElementById('generated_mutation_output').innerHTML = data["mutated_DNA"]
        },
        error: function (error){
            console.log(error);
        }
    })
})

