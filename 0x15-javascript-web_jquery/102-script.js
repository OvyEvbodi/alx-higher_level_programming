// Fetches and prints how to say “Hello” depending on the language

const url = 'https://www.fourtonfish.com/hellosalut/?';
const hello = $('div#hello');

$('document').ready(function () {
  $('input#btn_translate').click(getTranslation);
});

function getTranslation () {
  $.ajax({
  url: url + $.param({ lang: $('input#language_code').val() }),
  headers: {
    'Access-Control-Allow-Origin': '*'
  }
}).done((data, textStatus) => {
  if (textStatus === 'success')
    hello.html(data);
})
}
