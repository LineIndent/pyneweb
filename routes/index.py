import pynecone as pc
    
    
@pc.route(route='/', title='index')
def index():
    return pc.vstack(
        pc.hstack(
            
            width="100%",
            padding="5%",
            bg="blue",    
        ),
        # start #
pc.text('Hello! This is the', 
            pc.span(' index.py ', as_='mark'), 
            'page!!'),
            pc.hstack(
                pc.link('index', href='/'),
pc.link('contact', href='/contact'),
                width="100%",
                display='flex',
                align_items='center',
                justify_content='center',                
            ),
            # end #
        width="100%",
        height="100vh",
        box_sizing= "border-box",
    )
