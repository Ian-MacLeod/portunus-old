import { observer } from 'mobx-react';

import Layout from '@@/components/Layout';
import RegisterForm from '@@/components/Register';

const Register = () => {
  return (
    <Layout>
      <RegisterForm />
    </Layout>
  );
};

export default observer(Register);
