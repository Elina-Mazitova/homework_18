import allure
from selene import browser, be, have

from utils.api_client import post
from utils.ui_helpers import set_cookie


@allure.feature("Cart")
@allure.story("Add product to cart via API and verify via UI")
def test_add_to_cart_and_check_ui():
    product_id = 13

    response = post("/addproducttocart/details/13/1", data={"addtocart_13.EnteredQuantity": 1})
    cookie = response.cookies.get("Nop.customer")

    set_cookie("Nop.customer", cookie)

    browser.open("/cart")
    browser.element(".cart-item-row").should(be.visible)
    browser.element(".product-name").should(have.text("Computing and Internet"))


@allure.feature("Cart")
@allure.story("Add multiple products via API and verify via UI")
def test_add_multiple_products():
    products = {
        13: "Computing and Internet",
        31: "14.1-inch Laptop"
    }

    cookie = None

    for product_id, name in products.items():
        response = post(
            f"/addproducttocart/details/{product_id}/1",
            data={f"addtocart_{product_id}.EnteredQuantity": 1},
            cookies={"Nop.customer": cookie} if cookie else None
        )
        cookie = response.cookies.get("Nop.customer")

    set_cookie("Nop.customer", cookie)

    browser.open("/cart")

    for name in products.values():
        browser.all(".product-name").element_by(have.text(name)).should(be.visible)


@allure.feature("Cart")
@allure.story("Add same product twice via API and verify quantity")
def test_add_same_product_twice():
    product_id = 31

    response1 = post(
        f"/addproducttocart/details/{product_id}/1",
        data={f"addtocart_{product_id}.EnteredQuantity": 1}
    )
    cookie = response1.cookies.get("Nop.customer")

    response2 = post(
        f"/addproducttocart/details/{product_id}/1",
        data={f"addtocart_{product_id}.EnteredQuantity": 1},
        cookies={"Nop.customer": cookie}
    )

    set_cookie("Nop.customer", cookie)

    browser.open("/cart")

    browser.element(".product-name").should(have.text("14.1-inch Laptop"))
    browser.element(".qty-input").should(have.value("2"))
