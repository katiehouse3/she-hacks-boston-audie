## SheHacks Boston - Audie the Bear
#### Audie's Purpose:
Audie is a bear made to make **improve hospital experiences for children**. Audie's purpose is to facillitate discussions with children about feelings, especially for children who may experience difficulty expressing their feelings directly to adults. 

#### How Audie Helps: 
Audie's goal is for patients to feel heard, but not intimidated by their patient experience. Audie is a bear that is **activated by sound and records speech**. Patients will talk about how their is feeling and Audie will **encode their words into a sentiment value** once a recording has been made. This value reflects how positive or negative what the patient says is. From here, a **doctor can access the sentiment data** of the patient and make an assessment on the patient's progress.

#### How Audie Works:
Audie consists of three major components. The first component is the speech component. When someone speaks to the bear, a microphone will pick up the audio and record it to a file. We used an **Arduino board and it's sensors** to create the microphone set-up. The audio file is generated with **MATLAB**. The second component of the Audie project is the encoding and analysis of the data. We used the **Google Cloud Speech API** to take the audio file and transcribe to text. From there, the **Google Cloud Natural Language Processing API** is used with the text to calculate the sentiment of the patient. The data from the sentiment calculation is stored. The last component is the data visualization. We want a doctor to be able to look at the whole set of data for a patient, not just a particular day's score. The data points from the same patient are are all put on a line-graph, so a doctor can track the patients feelings over time.

<img src="https://challengepost-s3-challengepost.netdna-ssl.com/photos/production/software_photos/000/593/491/datas/gallery.jpg" height="300px;"></img>
