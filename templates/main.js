import React, { useState } from 'react';
import ReactDOM from 'react-dom';

function App() {
  const [predictedClass, setPredictedClass] = useState(null);

  const onFileChange = (event) => {
    const file = event.target.files[0];
    const formData = new FormData();
    formData.append('file', file);

    fetch('/upload', {
      method: 'POST',
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => {
        setPredictedClass(data.predicted_class);
      })
      .catch((error) => {
        console.error(error);
      });
  };

  return (
    <div>
      <input type="file" onChange={onFileChange} />
      {predictedClass !== null && (
        <p>Predicted class: {predictedClass}</p>
      )}
    </div>
  );
}

ReactDOM.render(<App />, document.getElementById('root'));