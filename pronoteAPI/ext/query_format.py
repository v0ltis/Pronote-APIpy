
base = {"infos": [],
        "user": {
                 "name": None,
                 "studentClass": {
                     "name": None
                 },
                 "establishmentsInfo": [{
                    "name": None,
                    "address": None,
                    "postalCode": None,
                    "city": None,
                    "website": None
                 }],
                 "userSettings": {
                    "version": None,
                    "theme": None,
                    "unreadDiscussions": None
                 },
                 "authorizations": {
                    "discussions": None,
                    "teachersDiscussions": None,
                    "timetableVisibleWeeks": None,
                    "canEditLessons": None,
                    "hideClassParts": None,
                    "maxEstablishmentFileSize": None,
                    "maxUserWorkFileSize": None,
                    "canPrint": None
                 }

             }}

empty = """{
    user {
        name
    }} """
"""Everything, except the name will be "None" or empyt list"""


full = """{
    infos {
        id
        date
        title
        author
        content
        htmlContent
        files {
            id
            name
            url
        }
    }
    user {
        name
        studentClass {
            name
        }
        establishmentsInfo{
            name
            address
            postalCode
            city
            website
        }
        userSettings{
            version
            theme
            unreadDiscussions
        }
        authorizations{
            discussions 
            teachersDiscussions 
            timetableVisibleWeeks
            canEditLessons 
            hideClassParts 
            maxEstablishmentFileSize 
            maxUserWorkFileSize 
            canPrint 
        }
     }}"""

homework = """{
        homeworks(from: \"%s\", to: \"%s\"){
            id
            description
            htmlDescription
            subject
            givenAt
            for
            done
            color
    }}"""
