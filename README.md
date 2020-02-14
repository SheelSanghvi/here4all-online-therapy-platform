# here4all-online-therapy-platform
Here4All is a web-application designed to help people facing various mental issues such as depression, anxiety, eating disorders, etc to connect with therapists online as well as have an access to a variety of mental health blogs. 
The main idea is to provide an alternative to the social taboo and pressure patients feel in attending therapy sessions in person. Also, this provides today's youth a way to deal with rising mental health problems in a positive way. 
Therapists and patients can communicate via chat using the web-app. Therapists can also add various blogs to the site and patients can have an access to all of them.

Since this is a fully equipped web-app with loads of features, i'll explain each of them individually:

HOME-PAGE

![image](https://user-images.githubusercontent.com/54235546/72379213-0123ac00-3739-11ea-82cd-90726ce15ff4.png)

The HomePage provides with a navigation bar with a self created logo and tabs for whytherapy, our team, blogs, register and sign in. There is short tagline and a JOIN US button linked to the register page.

WHY THERAPY SECTION

Slide 1

![image](https://user-images.githubusercontent.com/54235546/72379580-bbb3ae80-3739-11ea-96c7-6e78169c31af.png)

Slide 2

![image](https://user-images.githubusercontent.com/54235546/72379681-ea318980-3739-11ea-8f00-0f3bea457003.png)

Slide 3

![image](https://user-images.githubusercontent.com/54235546/72379708-f87fa580-3739-11ea-95de-f4f299e96b4e.png)

Quotes by few famous therapists to encourage people in taking therapy.

![image](https://user-images.githubusercontent.com/54235546/72379802-2238cc80-373a-11ea-9311-eb1e9756bb0d.png)

Writeup to encourage people towards therapy

![image](https://user-images.githubusercontent.com/54235546/72379875-4bf1f380-373a-11ea-8eb4-2e372ae098be.png)

![image](https://user-images.githubusercontent.com/54235546/72380008-8bb8db00-373a-11ea-8dd4-522c9105257b.png)

REGISTER PAGE

The Register Page considts of a form that asks for basic details required for account creation. There are two types of users in this webApp: patient and therapist.

![image](https://user-images.githubusercontent.com/54235546/72380111-bdca3d00-373a-11ea-8668-831355945231.png)

![image](https://user-images.githubusercontent.com/54235546/72380124-c6bb0e80-373a-11ea-94a6-5bb04f0223ab.png)

LOGIN PAGE

Once the user is created the page is redirected to the login page which asks for email and password from the user. if the details are valid and the user exists he/she is redirected to his/her dashboard.

![image](https://user-images.githubusercontent.com/54235546/72380488-84460180-373b-11ea-9c95-f1c3fc3100ce.png)

DASHBOARD OF PATIENT: Neeta Shah

![image](https://user-images.githubusercontent.com/54235546/72380516-97f16800-373b-11ea-9185-a6a7f2e6aa26.png)

The User can edit his personal details and also add a few like phone number and health issues faced. 

![image](https://user-images.githubusercontent.com/54235546/72380548-ad669200-373b-11ea-8a3e-fc2975e74d4c.png)

The edited/updated details are then updated to the profile page.

![image](https://user-images.githubusercontent.com/54235546/72380646-d850e600-373b-11ea-8fb5-10f9922596ab.png)

CONTACT DOCTOR

This is where the patient selects the doctor they wish to talk to and send their questions to the respective therapist. All past conversations are displayed on the same page stating the question asked by the patient, the answer received from the therapist and the therapist to whom the query was sent to.

![image](https://user-images.githubusercontent.com/54235546/72380692-f4ed1e00-373b-11ea-9324-8cc7fb38d880.png)

DASHBOARD OF THERAPIST: Manish Khanna

![image](https://user-images.githubusercontent.com/54235546/72380852-4b5a5c80-373c-11ea-98d5-3e28214aae5c.png)

This User can too edit/update his personal details.

CHAT WITH PATIENTS SECTION

All questions received by the therapist logged in are displayed here in the following format: Patient Nmae, Issues faced (question) and the answer submitted by the therapist for that query. If the answer is not yet submitted, a textfield will be displayed. Otherwise, the answer already submitted shall be displayed.

![image](https://user-images.githubusercontent.com/54235546/72380896-6200b380-373c-11ea-8a25-cf9d67df8cdb.png)

 ADD BLOGS SECTION
 
 Therapists can add blogs on a variety of topics in this section. These blogs shall be added to the main Blogs section which can be viewed by everyone - users and non-users. The Therapist logged in can also view his/her own blogs written in the past in the same page.
 
 ![image](https://user-images.githubusercontent.com/54235546/72381092-c3288700-373c-11ea-919b-9813a65f1402.png)

LOGOUT

Once the user logs out they are redirected to this logout page

![image](https://user-images.githubusercontent.com/54235546/72381266-231f2d80-373d-11ea-877f-9a9ca8a5570d.png)


BLOGS SECTION

Blogs written by therapists of here4all are displayed here viewable by everyone, both users and non-users of this webApp.

![image](https://user-images.githubusercontent.com/54235546/72381341-4649dd00-373d-11ea-8b11-b9ac0ceaf24d.png)

![image](https://user-images.githubusercontent.com/54235546/72381519-87da8800-373d-11ea-8e12-f42aa4af4d78.png)

![image](https://user-images.githubusercontent.com/54235546/72381560-97f26780-373d-11ea-8658-9cdf307b5460.png)

Blogs are also sorted according to topics. Example, Here we are in the eating disorders section.

![image](https://user-images.githubusercontent.com/54235546/72381598-a93b7400-373d-11ea-9e0e-c82fe3c8df2f.png)

OUR TEAM PAGE

This page displays all the therapists currently registered to here4all.

![image](https://user-images.githubusercontent.com/54235546/72381665-ca9c6000-373d-11ea-9af7-297b2ba3e210.png)

![image](https://user-images.githubusercontent.com/54235546/72381820-0df6ce80-373e-11ea-928f-07579ec3f582.png)

CONTACT US PAGE

Any person, user or non-user can submit general queries and questions they have through this form. It gets stored in the GuestContactUs Table in django admin. In production, a customer care team can review these queries and reply to the email id of the person who asked the query.

![image](https://user-images.githubusercontent.com/54235546/72381831-151ddc80-373e-11ea-9a21-d1af5930af10.png)

DJANGO ADMIN PAGE

User- to store both patient and therapist users.
Blog- to store blogs written by therapists
GuestContactUs- to store general queries from users/non-users.
Question- to store conversations between patients and therapists.

![image](https://user-images.githubusercontent.com/54235546/72381994-5ca46880-373e-11ea-85b7-d985625f64d3.png)

I've formatted the admin page (admin.py) with search fields and filter to suit to the developer's comfort.

![image](https://user-images.githubusercontent.com/54235546/72382330-0b48a900-373f-11ea-97bc-7728e501acf8.png)

Those were the features provided by the webApp. It is still under work. I will be adding a feature for the patients to save the blogs they like so that they can view them later, Searching facility, etc. Any suggestions/reviews are highly appreciated, email me at sanghvisheel@gmail.com

















