

certificates_vet = [
    { 
        "courses": [
            {
                "instituition": "Codenation",
                "name": "Aceleração Data Science",
                "hours": "80h",
                "year": "2020",
                "file": "certificates/courses/2020_codenation.pdf"
            },{
                "instituition": "Instituto Federal da Paraíba",
                "name": "Introdução a Deep Learning",
                "hours": "4h",
                "year": "2019",
                "file": "certificates/courses/2019_ifpb.pdf"
            },{
                "instituition": "Encontro Anual do Iecom em Comunicações, Redes e Criptografia",
                "name": "Processamento Digital de Imagens Aplicado À Engenharia Biomédica",
                "hours": "4h",
                "year": "2016",
                "file": "certificates/courses/2016_encom.pdf"
            },{
                "instituition": "Computar on the Beach",
                "name": "Jogos Multiplataforma com Cocos2d-x",
                "hours": "4h",
                "year": "2015",
                "file": "certificates/courses/2015_cotb.pdf"
            }
        ]
    },
    {
        "presentations": [
            {
                "instituition": "Codenation",
                "name": "Maratona Tecnologias móveis nas escolas",
                "hours": "80h",
                "year": "2010",
                "file": "certificates/presentations/maratona_unicef2018.pdf"
            },
            {
                "instituition": "Codenation",
                "name": "Maratona presentations móveis nas escolas",
                "hours": "80h",
                "year": "2010",
                "file": "certificates/presentations/maratona_unicef2018.pdf"
            }
        ]
    },
    {
        "awards": [
            {
                "instituition": "Sansumg and Unicef",
                "name": "Maratona Tecnologias móveis nas escolas",
                "hours": "24h",
                "year": "2018",
                "file": "certificates/awards/2018_unicef.pdf"
            },
            {
                "instituition": "Sociedade Brasileira de Computação",
                "name": "Olimpíada Brasileira de Informática",
                "description": "Honra ao mérito: 92/1119 participantes",
                "year": "2015",
                "file": "certificates/awards/2015_obi.pdf.pdf"
            },

        ]
    }
]


function loadCV(){
    let cv_file = "<a href=\"docs/cv_jose_raimundo_ptbr.pdf\" target=\"blank\">\"Baixe aqui o CV Resumido em PDF\"</a>"
    document.getElementById("cv_key").innerHTML = cv_file;
}

function loadCertificates() {
    let str_courses =  "";
    let str_presentations =  "";
    let str_awards =  "";
    certificates_vet.forEach(temp_certificate => {
        if (temp_certificate.courses){
            temp_certificate.courses.forEach( element =>{
                str_courses += "<li><i class=\"fa-li fa fa-list text-warning\"></i><a href=\"" +  element.file + "\" target=\"blank\">"+ element.year +" - "+ element.name +" - "+ element.instituition +"</a></li>";
            })
        }else if(temp_certificate.awards){
            temp_certificate.awards.forEach( element =>{
                str_awards += "<li><i class=\"fa-li fa fa-trophy text-warning\"></i><a href=\"" +  element.file + "\" target=\"blank\">"+ element.year +" - "+ element.name +" - "+ element.instituition +"</a></li>";
            })
        }else if(temp_certificate.presentations){
            temp_certificate.presentations.forEach( element =>{
                str_presentations += "<li><i class=\"fa-li fa fa-trophy text-warning\"></i><a href=\"" +  element.file + "\" target=\"blank\">"+ element.year +" - "+ element.name +" - "+ element.instituition +"</a></li>";
            })
        }
    })
    
    document.getElementById("courses_key").innerHTML = str_courses;
    document.getElementById("awards_key").innerHTML = str_awards;
    document.getElementById("presentations_key").innerHTML = str_presentations;
}
loadCertificates();