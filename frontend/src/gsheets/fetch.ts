export const fetchOTWPlan = async () => {
  fetch('/input_otw_plan/', {
    method: 'POST',
  })
    .then(response => response.json())
    .then(data => {
      console.log(data.message); // "Data inputted successfully!"
    })
    .catch(error => {
      console.error('There was an error!', error);
    });
};
