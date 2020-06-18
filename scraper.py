import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.ebay.com/itm/Sony-Alpha-a6000-Mirrorless-Digital-Camera-with-16-50mm-Lens-Black-16GB-Kit/331752774947?_trkparms=ispr%3D1&hash=item4d3e019d23:g:5KwAAOSwJ-ldHR9Z&enc=AQAFAAACcBaobrjLl8XobRIiIML1V4Imu%2Fn%2BzU5L90Z278x5ickkCrLl8erj3ATP5raQxjc%2F%2B8i5CKi7ihC97ixd0c0jYxJEjM5EIwwZIa39HAJA88jvq8kfiQhLoDrBJeHtzO%2BA2rKOvvfplQiGouJtcMku45o7Ni7J3RWGoPOb7THPC6b3ko0u0gslz0shZCD6KX4GGn5QOn7y3vClMPdju3S21buoUS0ShBh3%2B%2FVH9%2Fo7Sn0cZXXdnhav05n5JUKSEEBqrdE596TUkxE9m2h7aTkSRIrlWVf14i7abxlGLFhypxe82SnO5qWxaSeFFIX60nPrnR8xkDa4hRNVHK7IApmcMCnvyOAaui125WiqjyFxHjfjpBGzq73GY5ts1QLIPAEZWD14HWAQmWv6If8gyDpaZqwiDH1r8kVcpRFljbubCWa3MIFXENybNHyylYS44g8X7GdeY7f%2B8gPY8lbln1bHpdNGD8fQB6iwo5dhN4ewCTa38I949H7r%2Fcy6t8RcN4nehof7xabuPJ9yScA5vl6CLpsLhTxZsKLvK8Kpv5pMv5Zv9SskYIspDbh6BV712taVuKEk%2BlmxMNnJsCwCK0EQy8of7VkdUDPkh7WBM0dvggUtxpOW9YdisewBUSo%2FK1R1%2FNIaCwBa22X%2BUwt%2F14bBZb0KFSesOh2eUGcNYzWF5suIfszELkSOHKrX4NafCIWT4ZwwXFSgPr%2B1i94SqfJWfhO5OTIJGuB2sab9DNMSL%2FlrldoT8komSML%2FR1u8yTzc6u4j5xZ4K79QuOXKmnz0lPbwxa3LDJNtHF%2Fxn5dOFhia4aOTO9d9KGI%2Fm%2BsWRsy%2FTA%3D%3D&checksum=331752774947b9ba944cc0a6499a8ebf5e6246bd4abc'
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'}


def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, "html.parser")

    title = soup.find(id="itemTitle").get_text()
    price = soup.find(id="prcIsum").get_text()
    convertedprice = float(price[4:10])

    if convertedprice < 500.00:
        send_mail()

    print(convertedprice)
    print(title)

    if convertedprice > 500.00:
        send_mail()


def send_mail():
    server = smtplib.SMTP('rabnra@mail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('rabnra2019@mail.com', 'qwerty123')

    subject = 'Price fell down'
    body = 'Check the ebay link https://www.ebay.com/itm/Sony-Alpha-a6000-Mirrorless-Digital-Camera-with-16-50mm-Lens-Black-16GB-Kit/331752774947?_trkparms=ispr%3D1&hash=item4d3e019d23:g:5KwAAOSwJ-ldHR9Z&enc=AQAFAAACcBaobrjLl8XobRIiIML1V4Imu%2Fn%2BzU5L90Z278x5ickkCrLl8erj3ATP5raQxjc%2F%2B8i5CKi7ihC97ixd0c0jYxJEjM5EIwwZIa39HAJA88jvq8kfiQhLoDrBJeHtzO%2BA2rKOvvfplQiGouJtcMku45o7Ni7J3RWGoPOb7THPC6b3ko0u0gslz0shZCD6KX4GGn5QOn7y3vClMPdju3S21buoUS0ShBh3%2B%2FVH9%2Fo7Sn0cZXXdnhav05n5JUKSEEBqrdE596TUkxE9m2h7aTkSRIrlWVf14i7abxlGLFhypxe82SnO5qWxaSeFFIX60nPrnR8xkDa4hRNVHK7IApmcMCnvyOAaui125WiqjyFxHjfjpBGzq73GY5ts1QLIPAEZWD14HWAQmWv6If8gyDpaZqwiDH1r8kVcpRFljbubCWa3MIFXENybNHyylYS44g8X7GdeY7f%2B8gPY8lbln1bHpdNGD8fQB6iwo5dhN4ewCTa38I949H7r%2Fcy6t8RcN4nehof7xabuPJ9yScA5vl6CLpsLhTxZsKLvK8Kpv5pMv5Zv9SskYIspDbh6BV712taVuKEk%2BlmxMNnJsCwCK0EQy8of7VkdUDPkh7WBM0dvggUtxpOW9YdisewBUSo%2FK1R1%2FNIaCwBa22X%2BUwt%2F14bBZb0KFSesOh2eUGcNYzWF5suIfszELkSOHKrX4NafCIWT4ZwwXFSgPr%2B1i94SqfJWfhO5OTIJGuB2sab9DNMSL%2FlrldoT8komSML%2FR1u8yTzc6u4j5xZ4K79QuOXKmnz0lPbwxa3LDJNtHF%2Fxn5dOFhia4aOTO9d9KGI%2Fm%2BsWRsy%2FTA%3D%3D&checksum=331752774947b9ba944cc0a6499a8ebf5e6246bd4abc'

    msg = f"Subject: {subject} \n \n {body}"

    server.sendmail(
        'rabnra@mail.com',
        'rabnra2019@gmail.com',
        msg)
    print('Hey email has been sent!')

    server.quit()


check_price()
