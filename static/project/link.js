const contentMain = document.getElementById('content-main');
const div = document.createElement('div');

const ul = document.createElement('ul');
ul.setAttribute('id', 'link-schedule');

const targetUrl = 'http://ec2-35-164-231-211.us-west-2.compute.amazonaws.com';
const links = [
    {name: 'TV 1 - Monday - Thuesday', link: `${targetUrl}/monday-thuesday-vertical/`},
    {name: 'TV 2 - Wednesday - Thursday', link: `${targetUrl}/wenesday-thursday-vertical/`},
    {name: 'TV 3 - Friday - Saturday', link: `${targetUrl}/friday-saturday-vertical/`},
    {name: 'TV 4 - Sunday', link: `${targetUrl}/sunday-next_monday-vertical/`}
];

links.forEach(address => {
    const li = document.createElement('li');
    const link = document.createElement('a');
    customElement(link, address.link, address.name);
    li.appendChild(link);
    ul.appendChild(li);
});

div.appendChild(ul);
contentMain.appendChild(div);

function customElement (link, address, name){
    link.href = address;
    link.textContent = name;
    link.setAttribute('target', '__blank');
    link.style.color = '#331935';
}

if (location.pathname !== '/' && location.pathname !== '/schedule/')
    div.remove();
