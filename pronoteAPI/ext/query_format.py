class Querys:

    empty_awnser = {}

    all = """{
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
