import { useState } from 'react'
import gambar1 from '/gambar1-sub-cntn-informasi-1.png'
import gambar2 from '/gambar2-sub-cntn-informasi-1.png'
import gambar3 from '/gambar3-sub-cntn-informasi-1.png'
import gambar4 from '/gambar4-sub-cntn-informasi-1.png'
import gambar5 from '/gambar1-sub-cntn-informasi-2.png'
import gambar6 from '/gambar2-sub-cntn-informasi-2.png'
import gambar7 from '/gambar3-sub-cntn-informasi-2.png'
import gambar8 from '/gambar4-sub-cntn-informasi-2.png'
import gambar9 from '/gambar5-sub-cntn-informasi-2.png'
import gambar10 from '/gambar6-sub-cntn-informasi-2.png'
import Logo from '/Icon.png'
import './App.css'

function App() {
  // const [Nama_Pengirim, setName] = useState([]);
  // const [Email_Pengirim, setEmail] = useState("");
  // const [Pesan_Pengirim, setPesan] = useState({});

  // const kirimContactUs = async () => {
  //   const dataContactUs = {
  //     Nama_Pengirim,
  //     Email_Pengirim,
  //     Pesan_Pengirim,
  //   };
  //   try{
  //     const response = await fetch("http:127.0.0.1:8000/SampahAPP/ContactUs/create/", {
  //       method: "POST",
  //       headers: {
  //         "Content-Type":"application/jason",
  //       },
  //       body: JSON.stringify(dataContactUs),
  //     });
  //     const data = await response.json();
  //     setName((prev)=>[...prev, data]);
  //   }catch (err){
  //     console.log(err);
  //   }
  // };
  return (
    <>
      <div className='Navbar'>
        <div className='Merk'>
          <img src="/Icon.png" className='Logo'/>
          <h2>Trash Us</h2>
        </div>
        <div className='Menu'>
          <a href="#">Beranda</a>
          <a href="#">Informasi</a>
          <a href="#">Peta Kami</a>
          <a href="#">Contact Us</a>
        </div>
        <div className='Log_Sign'>
          <button><b>Log In</b></button>
          <button><b>Sign In</b></button>
        </div>
      </div>
      <div className='Beranda' id='Beranda'>
        <div className='Judul'>
          <h1>Small Action, Big Impact</h1>
        </div>
        <div className='Text'>
          <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Enim ipsa maxime eligendi tempora quos vero totam aspernatur ex, quis consectetur ea id sapiente nemo aperiam cumque saepe facilis perspiciatis est!</p>
        </div>
        <div className='btn-beranda'>
        <button className='btn-b'>Learn More</button>
        </div>
      </div>
      <div className='Informasi' id='Informasi'>
        <div className='cntn-1-informasi'>
          <h2>Sistem Pengelolaan Sampah</h2>
          <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Sapiente dolor, labore iusto repudiandae commodi cum. Nobis et modi vitae quam deleniti qui sapiente aliquid dolor, officia iusto praesentium, sit possimus!</p>
        </div>
        <div className='cntn-2-informasi'>
          <h2>Cara Bergabung Dengan Trash Us</h2>
          <div className='sub-cntn-2-informasi'>
            <div className='poin'>
              <div className='bg-gambar-sub-cntn-2-informasi'>
                <img className='gambar-cntn-2-infomasi' src="/gambar1-sub-cntn-informasi-1.png" alt="" />
              </div>
              <p>Pendaftaran</p>
            </div>
            <div className='poin'>
              <div className='bg-gambar-sub-cntn-2-informasi'>
                <img className='gambar-cntn-2-infomasi' src="/gambar2-sub-cntn-informasi-1.png" alt="" />
              </div>
              <p>Pengumpulan</p>
            </div>
            <div className='poin'>
              <div className='bg-gambar-sub-cntn-2-informasi'>
                <img className='gambar-cntn-2-infomasi' src="/gambar3-sub-cntn-informasi-1.png" alt="" />
              </div>
              <p>Pemilahan</p>
            </div>
            <div className='poin'>
              <div className='bg-gambar-sub-cntn-2-informasi'>
                <img className='gambar-cntn-2-infomasi' src="/gambar4-sub-cntn-informasi-1.png" alt="" />
              </div>
              <p>Keuntungan</p>
            </div>
          </div>
        </div>
      </div>
      <div className='Informasi-2' id='informasi-2'>
        <h2>Berita Dan Infromasi Tentang Sampah</h2>
        <div className='cntn-1-informasi-2'>
          <div className='sub-cntn-informasi-2'>
            <img src="/gambar1-sub-cntn-informasi-2.png" alt="" />
            <h3>bla-bla-bla</h3>
            <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Magnam sunt illum omnis eveniet autem inventore, quam numquam fuga dolorem temporibus, ducimus consectetur quasi aliquid deserunt eius perferendis ut doloribus officiis.</p>
          </div>
          <div className='sub-cntn-informasi-2'>
            <img src="/gambar2-sub-cntn-informasi-2.png" alt="" />
            <h3>bla-bla-bla</h3>
            <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Magnam sunt illum omnis eveniet autem inventore, quam numquam fuga dolorem temporibus, ducimus consectetur quasi aliquid deserunt eius perferendis ut doloribus officiis.</p>
          </div>
          <div className='sub-cntn-informasi-2'>
            <img src="/gambar3-sub-cntn-informasi-2.png" alt="" />
            <h3>bla-bla-bla</h3>
            <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Magnam sunt illum omnis eveniet autem inventore, quam numquam fuga dolorem temporibus, ducimus consectetur quasi aliquid deserunt eius perferendis ut doloribus officiis.</p>
          </div>
        </div>
        <div className='cntn-2-informasi-2'>
          <div className='sub-cntn-informasi-2'>
              <img src="/gambar4-sub-cntn-informasi-2.png" alt="" />
              <h3>bla-bla-bla</h3>
              <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Magnam sunt illum omnis eveniet autem inventore, quam numquam fuga dolorem temporibus, ducimus consectetur quasi aliquid deserunt eius perferendis ut doloribus officiis.</p>
            </div>
            <div className='sub-cntn-informasi-2'>
              <img src="/gambar5-sub-cntn-informasi-2.png" alt="" />
              <h3>bla-bla-bla</h3>
              <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Magnam sunt illum omnis eveniet autem inventore, quam numquam fuga dolorem temporibus, ducimus consectetur quasi aliquid deserunt eius perferendis ut doloribus officiis.</p>
            </div>
            <div className='sub-cntn-informasi-2'>
              <img src="/gambar6-sub-cntn-informasi-2.png" alt="" />
              <h3>bla-bla-bla</h3>
              <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Magnam sunt illum omnis eveniet autem inventore, quam numquam fuga dolorem temporibus, ducimus consectetur quasi aliquid deserunt eius perferendis ut doloribus officiis.</p>
            </div>
        </div>
      </div>
      <div className='ContactUs' id='ContactUs'>
        <div className='cntn-1-ContactUs'>
          <h1>Hubungi Kami Disini</h1>
          <div className='sub-cntn-1-ContactUs'>
            <img src="" alt="" />
            <p>Bandung, Jalan Geger Kalong No.2</p>
          </div>
          <div className='sub-cntn-1-ContactUs'>
            <img src="" alt="" />
            <p>(+62)82123456789</p>
          </div>
          <div className='sub-cntn-1-ContactUs'>
            <img src="" alt="" />
            <p>banksampahbandung@gmail.com</p>
          </div>
        </div>
        <div className='cntn-2-ContactUs'>
          <form method='post'>
            <label name="Nama_ContactUs">Nama Lengkap</label>
            {/* onChange={(e) => setName(e.target.value)} */}
            <input type="text" name='Nama_ContactUs' id='Nama_ContactUs' />
            <label name="Email_ContactUs">Email</label>
            {/* onChange={(e) => setEmail(e.target.value)} */}
            <input type="email" name='Email_ContactUs' id='Email_ContactUs' />
            <label name="Pesan_ContactUs">Pesan</label>
            {/* onChange={(e) => setPesan(e.target.value)} */}
            <textarea name="Pesan_ContactUs" id="Pesan_ContactUs" ></textarea>
            <div >
              {/* <button onClick={kirimContactUs}>Kirim</button> */}
              <input type="submit" value="Kirim" className='submit' />
              </div>  
          </form>
        </div>
      </div>
      <div className='Footer'>
          <div className='sub-footer'>
            <img src="" alt="" />
            <a href="#">banksampahbdg_</a>
          </div>
          <div className='sub-footer'>
            <img src="" alt="" />
            <a href="#">banksampahbdg_</a>
          </div>
          <div className='sub-footer'>
            <img src="" alt="" />
            <a href="#">banksampahbdg_</a>
          </div>
        </div>
    </>
  )
}

export default App
