// Fetches from https://fourtonfish.com/hellosalut/?lang=fr
// and displays the value of hello from that fetch in the HTML tag DIV#hello 

const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
const hello = $('div#hello');

$.ajax({
  url: url,
  headers: {
    'Access-Control-Allow-Origin': '*'
  }
}).done((data, textStatus) => {
  if (textStatus === 'success')
    hello.text(data);
})
